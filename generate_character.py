import random
import argparse
import sys

# 依存するスクリプトから必要な関数をインポート
from fantasy_role_analyzer import suggest_combat_basic_roles, suggest_general_basic_roles, get_eligible_advanced_roles

# 定義ファイルをインポート
from character_constants import *


def generate_full_name(race, gender):
    """指定された種族と性別に基づいてフルネームを生成する"""
    if race not in FIRST_NAMES or race not in FAMILY_NAMES:
        raise ValueError(f"未知の種族です: {race}")
    if gender not in GENDERS or gender not in FIRST_NAMES[race]:
        raise ValueError(f"未知の性別、またはその種族に定義されていない性別です: {gender} (種族: {race})")

    first_name = random.choice(FIRST_NAMES[race][gender])
    family_name = random.choice(FAMILY_NAMES[race])
    return f"{first_name}・{family_name}"


def get_random_sacred_name():
    """聖なる名前をランダムに取得する"""
    return random.choice(SACRED_NAMES)


# 能力値生成関連の定数と関数
STATUS_NAMES = ["腕力", "耐久", "持久力", "敏捷", "照準力", "魔力", "魔法抵抗", "信仰", "統率", "騎乗",
                "学力", "機転", "政治力", "調理", "味覚", "芸術", "工作", "社交性", "魅力", "幸運"]
COMBAT_STATUS_COUNT = 10  # 戦闘系能力値の数 (STATUS_NAMESの前半)

# 種族別の得意・苦手能力を定義
RACE_STATS_MODIFIERS = {
    "人間族": {
        "weak": [],
        "strong": []
    },
    "エルフ族": {
        "weak": ["腕力", "耐久", "政治力"],
        "strong": ["魔力", "照準力", "学力"]
    },
    "ドワーフ族": {
        "weak": ["敏捷", "騎乗", "社交性"],
        "strong": ["腕力", "耐久", "工作"]
    },
    "獣人族": {
        "weak": ["学力", "政治力", "魔力"],
        "strong": ["腕力", "敏捷", "持久力"]
    },
    "鳥人族": {
        "weak": ["腕力", "耐久", "工作"],
        "strong": ["機転", "騎乗", "芸術"]
    },
    "竜人族": {
        "weak": ["調理", "芸術", "社交性"],
        "strong": ["統率", "耐久", "魔法抵抗"]
    },
    "妖精族": {
        "weak": ["腕力", "耐久", "持久力"],
        "strong": ["魔力", "魅力", "幸運"]
    },
    "人魚族": {
        "weak": ["腕力", "持久力", "幸運"],
        "strong": ["魔力", "騎乗", "魅力"]
    }
}


def generate_normal_value(mu, sigma, min_val, max_val):
    """指定された範囲内に収まるように正規分布から値を生成するヘルパー関数"""
    temp_value = random.normalvariate(mu, sigma)
    return max(min_val, min(max_val, round(temp_value)))


def generate_statuses_strict_one_talent(status_names, race, base_mu=50, base_sigma=19.4):
    """
    厳密に1つだけ91以上の特別な才能を持つように能力値を生成する関数。
    種族ごとの得意・苦手能力を考慮し、正規分布ベースで値を生成する。
    """
    if not status_names:
        return {}

    race_mods = RACE_STATS_MODIFIERS.get(race, {"weak": [], "strong": []})
    derived_sigma = base_sigma / 2
    statuses = {}
    high_status_abilities = []

    for name in status_names:
        if name in race_mods["weak"]:
            init_value = generate_normal_value(25, derived_sigma, 0, 50) if random.random() > 0.1 else random.randint(
                91, 100)
        elif name in race_mods["strong"]:
            init_value = generate_normal_value(75, derived_sigma, 50, 100)
        else:
            init_value = generate_normal_value(base_mu, base_sigma, 0, 100)
        statuses[name] = int(init_value)
        if statuses[name] >= 91:
            high_status_abilities.append(name)

    num_high_statuses = len(high_status_abilities)
    if num_high_statuses == 0 and status_names:
        eligible_statuses_for_talent = list(statuses.keys())
        if eligible_statuses_for_talent:
            status_to_enhance = random.choice(eligible_statuses_for_talent)
            statuses[status_to_enhance] = random.randint(91, 100)
    elif num_high_statuses > 1:
        talent_to_keep = random.choice(high_status_abilities)
        for name_to_adjust in high_status_abilities:
            if name_to_adjust != talent_to_keep:
                if name_to_adjust in race_mods["weak"]:
                    adjusted_value = generate_normal_value(25, derived_sigma, 0, 50)
                elif name_to_adjust in race_mods["strong"]:
                    sigma_for_strong_degrade = base_sigma * 0.4
                    adjusted_value = generate_normal_value(70, sigma_for_strong_degrade, 50, 90)
                else:
                    sigma_for_normal_degrade = base_sigma * 0.9
                    adjusted_value = generate_normal_value(45, sigma_for_normal_degrade, 0, 90)
                statuses[name_to_adjust] = int(adjusted_value)
    return statuses


# 装備関連
EQUIPMENT_TYPES = {
    "剣": "腕力", "鎧": "耐久", "靴": "敏捷", "杖": "魔力",
    "ローブ": "魔法抵抗", "指輪": "魅力", "護符": "幸運"
}
EQUIPMENT_NAMES = list(EQUIPMENT_TYPES.keys())


def get_ethics_alignment_name(ethic_value):
    """倫理観の数値から対応するカテゴリ名を取得する(5x5対応)"""
    if 81 <= ethic_value <= 100:
        return "Strong Lawful"
    elif 61 <= ethic_value <= 80:
        return "Lawful"
    elif 40 <= ethic_value <= 60:
        return "Neutral"
    elif 20 <= ethic_value <= 39:
        return "Chaotic"
    elif 0 <= ethic_value <= 19:
        return "Strong Chaotic"
    return "Unknown"


def get_morality_alignment_name(moral_value):
    """道徳観の数値から対応するカテゴリ名を取得する(5x5対応)"""
    if 81 <= moral_value <= 100:
        return "Noble"
    elif 61 <= moral_value <= 80:
        return "Good"
    elif 40 <= moral_value <= 60:
        return "Neutral"
    elif 20 <= moral_value <= 39:
        return "Evil"
    elif 0 <= moral_value <= 19:
        return "Vile"
    return "Unknown"


def generate_character_raw_data(gender_choice=None, race_choice=None, ethics_choice=None, morality_choice=None):
    """
    キャラクターの基本データを生成する関数。
    指定されたパラメータ、またはランダムな値を使用する。
    """
    race = race_choice if race_choice and race_choice in RACES else random.choice(RACES)
    gender = gender_choice if gender_choice and gender_choice in GENDERS else random.choice(GENDERS)
    name = generate_full_name(race, gender)

    base_age = random.randint(10, 60)
    age = base_age
    human_equivalent_age = base_age
    if race in ["竜人族", "ドワーフ族"]:
        age *= 5
    elif race == "エルフ族":
        age *= 20

    height = round(random.normalvariate(160, 17.37))
    height = max(120, min(200, height))
    if race == "竜人族":
        height += 50
    elif race == "ドワーフ族":
        height -= 50
    elif race == "妖精族":
        height -= 100
    # 人魚族の身長は人間モードを想定し、人間族の基準と同じにする

    # 倫理観 (Ethics) - 5x5対応
    ethics = 50
    if ethics_choice and ethics_choice in ETHICS_ALIGNMENTS:
        if ethics_choice == "Strong Chaotic":
            ethics = random.randint(0, 19)
        elif ethics_choice == "Chaotic":
            ethics = random.randint(20, 39)
        elif ethics_choice == "Neutral":
            ethics = random.randint(40, 60)
        elif ethics_choice == "Lawful":
            ethics = random.randint(61, 80)
        elif ethics_choice == "Strong Lawful":
            ethics = random.randint(81, 100)
    else:
        ethics = round(random.normalvariate(50, 19.4))
        ethics = max(0, min(100, ethics))
    ethics_alignment_name = get_ethics_alignment_name(ethics)

    # 道徳観 (Morality) - 5x5対応
    morality = 50
    if morality_choice and morality_choice in MORALITY_ALIGNMENTS:
        if morality_choice == "Vile":
            morality = random.randint(0, 19)
        elif morality_choice == "Evil":
            morality = random.randint(20, 39)
        elif morality_choice == "Neutral":
            morality = random.randint(40, 60)
        elif morality_choice == "Good":
            morality = random.randint(61, 80)
        elif morality_choice == "Noble":
            morality = random.randint(81, 100)
    else:
        morality = round(random.normalvariate(50, 19.4))
        morality = max(0, min(100, morality))
    morality_alignment_name = get_morality_alignment_name(morality)

    statuses = generate_statuses_strict_one_talent(STATUS_NAMES, race)

    # 種族に応じて「騎乗」を「飛行」または「遊泳」に変換
    if race in ["鳥人族", "妖精族"]:
        if "騎乗" in statuses:
            statuses["飛行"] = statuses.pop("騎乗")
    elif race == "人魚族":
        if "騎乗" in statuses:
            statuses["遊泳"] = statuses.pop("騎乗")

    equipment_name_str = "なし"
    equipment_info = None
    if random.random() < 0.1:
        item_type = random.choice(EQUIPMENT_NAMES)
        sacred_name_for_item = get_random_sacred_name()
        equipment_name_str = f"{sacred_name_for_item}の{item_type}"
        status_to_buff = EQUIPMENT_TYPES[item_type]
        statuses[status_to_buff] = min(100, statuses[status_to_buff] + 10)
        equipment_info = {"name": equipment_name_str, "type": item_type, "buffed_status": status_to_buff}

    # 合計値計算の前に、表示用のステータスリストを種族に応じて調整
    display_status_names = STATUS_NAMES.copy()
    if race in ["鳥人族", "妖精族"]:
        if "騎乗" in display_status_names:
            display_status_names[display_status_names.index("騎乗")] = "飛行"
    elif race == "人魚族":
        if "騎乗" in display_status_names:
            display_status_names[display_status_names.index("騎乗")] = "遊泳"

    combat_status_total = sum(statuses[s] for s in display_status_names[:COMBAT_STATUS_COUNT] if s in statuses)
    general_status_total = sum(statuses[s] for s in display_status_names[COMBAT_STATUS_COUNT:] if s in statuses)

    return {
        "name": name,
        "race": race,
        "gender": gender,
        "age": age,
        "human_equivalent_age": human_equivalent_age,
        "height": height,
        "statuses": statuses,
        "equipment_name": equipment_name_str,
        "equipment_info": equipment_info,
        "combat_status_total": combat_status_total,
        "general_status_total": general_status_total,
        "ethics": ethics,
        "ethics_alignment": ethics_alignment_name,  # 表示用にカテゴリ名を保持
        "morality": morality,
        "morality_alignment": morality_alignment_name,  # 表示用にカテゴリ名を保持
    }


def get_user_choice(prompt, options, allow_random=True, random_text="ランダム"):
    """ユーザーに選択肢を提示し、入力を受け付ける関数"""
    print(f"\n{prompt}")
    for option_num, option in enumerate(options):
        print(f"{option_num + 1}. {option}")
    if allow_random:
        print(f"{len(options) + 1}. {random_text}")

    while True:
        try:
            choice_input = input(f"選択してください (1-{len(options) + (1 if allow_random else 0)}): ")
            if not choice_input:
                if allow_random:
                    return "ランダム"
                else:
                    print("入力が必要です。")
                    return None

            choice_num = int(choice_input)
            if 1 <= choice_num <= len(options):
                return options[choice_num - 1]
            elif allow_random and choice_num == len(options) + 1:
                return "ランダム"
            else:
                print("無効な選択です。もう一度入力してください。")
        except ValueError:
            print("数値を入力してください。")
        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")


def display_character(char_raw_data):
    """生成されたキャラクターデータと推奨ロールをコンソールに表示する関数"""
    print("\n--- 生成されたキャラクターデータ ---")
    ethics_align_name = char_raw_data.get('ethics_alignment', '')
    morality_align_name = char_raw_data.get('morality_alignment', '')

    race_for_display = char_raw_data.get('race')
    display_sample_names = STATUS_NAMES.copy()
    if race_for_display in ["鳥人族", "妖精族"]:
        if "騎乗" in display_sample_names:
            display_sample_names[display_sample_names.index("騎乗")] = "飛行"
    elif race_for_display == "人魚族":
        if "騎乗" in display_sample_names:
            display_sample_names[display_sample_names.index("騎乗")] = "遊泳"

    for key, value in char_raw_data.items():
        if key == "statuses":
            print(f"  {key}:")

            combat_statuses_str = []
            general_statuses_str = []

            talented_status_name = None
            for status_name_iter, status_value_iter in value.items():
                if status_value_iter >= 91:
                    talented_status_name = status_name_iter
                    break

            for status_num, status_name in enumerate(display_sample_names):
                if status_name in value:
                    status_value = value[status_name]
                    display_value_str = str(status_value)

                    if status_name == talented_status_name:
                        display_value_str = f"**{status_value}**"
                    elif int(status_value) <= 10:
                        display_value_str = f"*{status_value}*"

                    if status_num < COMBAT_STATUS_COUNT:
                        combat_statuses_str.append(f"{status_name}: {display_value_str}")
                    else:
                        general_statuses_str.append(f"{status_name}: {display_value_str}")

            print(f"    戦闘系: {', '.join(combat_statuses_str)}")
            print(f"    一般系: {', '.join(general_statuses_str)}")

        elif key == "equipment_info" and value:
            print(
                f"    (装備詳細: Type={value['type']}, Buffs={value['buffed_status']})")
        elif key == "equipment_info" and not value:
            pass
        elif key == "ethics":
            print(f"  ethics: {value}")
        elif key == "morality":
            print(f"  morality: {value}")
        elif key in ["ethics_alignment", "morality_alignment"]:
            pass
        else:
            print(f"  {key}: {value}")

    if ethics_align_name and morality_align_name:
        print(f"  alignment: {ethics_align_name} {morality_align_name}")

    print("-" * 30)
    
    # --- ▼▼▼ ロール分析と表示機能を追加 ▼▼▼ ---
    print("\n--- 推奨ロール分析 ---")

    abilities = char_raw_data['statuses']
    ethics = char_raw_data['ethics']
    morality = char_raw_data['morality']

    # 1. 戦闘系基本ロールの推奨
    print("\n[戦闘系基本ロール おすすめ TOP 3]")
    suggested_combat = suggest_combat_basic_roles(abilities)
    if suggested_combat:
        for role in suggested_combat:
            details_str = ", ".join([f"{k}: {v}" for k, v in role['details'].items()])
            print(f"  - {role['name']} (適性スコア: {role['score']:.1f})")
            print(f"    適性能力: {details_str}")
            print(f"    概要: {role['description']}")
    else:
        print("  (適性のあるロールが見つかりませんでした)")

    # 2. 一般系基本ロールの推奨
    print("\n[一般系基本ロール おすすめ TOP 3]")
    suggested_general = suggest_general_basic_roles(abilities)
    if suggested_general:
        for role in suggested_general:
            details_str = ", ".join([f"{k}: {v}" for k, v in role['details'].items()])
            print(f"  - {role['name']} (適性スコア: {role['score']:.1f})")
            print(f"    適性能力: {details_str}")
            print(f"    概要: {role['description']}")
    else:
        print("  (適性のあるロールが見つかりませんでした)")

    # 3. 就任可能な派生・特殊ロール
    print("\n[就任可能な派生・特殊ロール]")
    eligible_advanced = get_eligible_advanced_roles(abilities, ethics, morality)
    if eligible_advanced:
        for role in eligible_advanced:
            print(f"  - {role['name']}")
            print(f"    概要: {role['description']}")
    else:
        print("  (条件を満たすロールはありません)")
        
    print("-" * 30)
    # --- ▲▲▲ ロール分析と表示機能ここまで ▲▲▲ ---


def run_interactive_mode():
    """対話形式でキャラクターを生成する関数"""
    print("ファンタジーキャラクターを生成します。")
    print("------------------------------------")

    generation_mode = get_user_choice(
        "生成モードを選択してください:",
        ["全てランダムに生成", "詳細を指定して生成"],
        allow_random=False
    )

    params = {
        "gender_choice": None,
        "race_choice": None,
        "ethics_choice": None,
        "morality_choice": None,
    }

    if generation_mode == "詳細を指定して生成":
        print("\n--- 詳細設定 ---")
        print("各項目でEnterキーのみを押すと「ランダム」が選択されます。")

        chosen_gender = get_user_choice("性別を選択してください:", GENDERS, random_text="ランダムな性別")
        if chosen_gender != "ランダム":
            params["gender_choice"] = chosen_gender

        chosen_race = get_user_choice("種族を選択してください:", RACES, random_text="ランダムな種族")
        if chosen_race != "ランダム":
            params["race_choice"] = chosen_race

        chosen_ethics = get_user_choice("倫理観を選択してください:", ETHICS_ALIGNMENTS, random_text="ランダムな倫理観")
        if chosen_ethics != "ランダム":
            params["ethics_choice"] = chosen_ethics

        chosen_morality = get_user_choice("道徳観を選択してください:", MORALITY_ALIGNMENTS,
                                          random_text="ランダムな道徳観")
        if chosen_morality != "ランダム":
            params["morality_choice"] = chosen_morality
    
    print("\n--- 生成中 ---")
    char_raw_data = generate_character_raw_data(**params)
    display_character(char_raw_data)

def create_help_text(options_list):
    """選択肢のリストからヘルプ文字列を生成する"""
    return "0: ランダム, " + ", ".join([f"{i+1}: {option}" for i, option in enumerate(options_list)])


if __name__ == '__main__':
    # コマンドライン引数のパーサーを設定
    parser = argparse.ArgumentParser(
        description='ファンタジーキャラクターを生成します。引数なしで実行すると対話モードになります。',
        formatter_class=argparse.RawTextHelpFormatter # ヘルプメッセージの改行を維持
    )

    # ヘルプメッセージ用の文字列を生成
    gender_help = create_help_text(GENDERS)
    race_help = create_help_text(RACES)
    ethics_help = create_help_text(ETHICS_ALIGNMENTS)
    morality_help = create_help_text(MORALITY_ALIGNMENTS)

    # 数値で引数を指定できるように変更
    parser.add_argument('--gender', help=f'キャラクターの性別を数値で指定:\n  {gender_help}', type=int, choices=range(0, len(GENDERS) + 1))
    parser.add_argument('--race', help=f'キャラクターの種族を数値で指定:\n  {race_help}', type=int, choices=range(0, len(RACES) + 1))
    parser.add_argument('--ethics', help=f'キャラクターの倫理観を数値で指定:\n  {ethics_help}', type=int, choices=range(0, len(ETHICS_ALIGNMENTS) + 1))
    parser.add_argument('--morality', help=f'キャラクターの道徳観を数値で指定:\n  {morality_help}', type=int, choices=range(0, len(MORALITY_ALIGNMENTS) + 1))

    # 引数が1つだけ（スクリプト名のみ）の場合は対話モードを起動
    if len(sys.argv) == 1:
        run_interactive_mode()
    else:
        # 引数が存在する場合は、それを解析してキャラクターを生成
        args = parser.parse_args()

        # 数値から対応する文字列に変換
        gender_choice = GENDERS[args.gender - 1] if args.gender else None
        race_choice = RACES[args.race - 1] if args.race else None
        ethics_choice = ETHICS_ALIGNMENTS[args.ethics - 1] if args.ethics else None
        morality_choice = MORALITY_ALIGNMENTS[args.morality - 1] if args.morality else None

        params = {
            "gender_choice": gender_choice,
            "race_choice": race_choice,
            "ethics_choice": ethics_choice,
            "morality_choice": morality_choice,
        }

        print("\n--- 引数に基づいてキャラクターを生成中 ---")
        char_raw_data = generate_character_raw_data(**params)
        display_character(char_raw_data)