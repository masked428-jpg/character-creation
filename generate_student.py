import random
import argparse
import sys

# ブルーアーカイブの生徒の年齢範囲
BLUEARCHIVE_AGE_MIN = 15
BLUEARCHIVE_AGE_MAX = 17

# 名前生成のために便宜上「生徒」のリストを使用
PLACEHOLDER_RACE_FOR_NAME = "生徒"

FIRST_NAMES_BLUEARCHIVE = {
    "生徒": [
        "アイカ", "ショウコ", "ツグミ", "アキコ", "チヅコ", "マユミ", "メイ", "ユイカ", "ユウキ", "アイラ", "アキ",
        "マヨ", "アン", "エマ", "オトエ", "カオリ", "キミコ", "ケイコ", "ココア", "シオ", "スミコ", "ヒロコ",
        "マサコ", "アリサ", "ミチコ", "ミナミ", "ミホ", "ユウ", "ユマ", "リイサ", "アイ", "アオナ", "アキカ",
        "アコウ", "アスカ", "アマネ", "アミ", "カオルコ", "アヤカ", "アユナ", "アリ", "アルル", "アンナ", "イオ",
        "イクコ", "イノリ", "ウタウ", "ウタネ", "ウレシ", "エオリ", "エカ", "エツカ", "エミコ", "エリイ", "エリホ",
        "オトカ", "オトミ", "オリネ", "カズヨ", "カノ", "カセン", "アモ", "カツコ", "カナミ", "カノリ", "カハ",
        "カホノ", "カホリ", "カユコ", "キアメ", "キエコ", "キミ", "キエミ", "キオコ", "キスミ", "キヒロ", "キユキ",
        "キョウ", "キラエ", "キルイ", "クイ", "クニエ", "クミ", "クモ", "ケイカ", "コア", "コウミ", "ココミ",
        "コスズ", "コハク", "コマチ", "コユウ", "サカ", "サキカ", "サキネ", "サチコ", "サトミ", "サヤカ", "サヤノ",
        "サヨリ", "シアヤ", "シゲコ", "シズカ", "シトカ", "シノ", "シノル", "ジユウ", "シユキ", "シュンリ", "ジン",
        "スズエ", "スズノ", "スズメ", "スバル", "スリカ", "セイコ", "セツキ", "ソウア", "ソウカ", "タホ", "ソリン",
        "タエコ", "タカコ", "タクエ", "タマミ", "タマリ", "チカ", "チカエ", "チカコ", "ツグハ", "テルコ", "テルノ",
        "チヨ", "テル", "トウカ", "トキコ", "トトミ", "トモコ", "トヨ", "ナキ", "ナコ", "ナツキ", "ナヅキ", "ナナ",
        "ナユ", "ナナコ", "ナリミ", "ナルカ", "ナルキ", "ニツル", "ネナ", "ノジコ", "ノブエ", "ノブカ", "ノブコ",
        "ノラン", "ノリエ", "ノリコ", "ハアイ", "ハズエ", "ハヤカ", "ハユカ", "ヒア", "ヒサナ", "ヒソラ", "ヒトミ",
        "ヒナノ", "ヒビセ", "ヒロミ", "ヒヨ", "フキノ", "フクヨ", "フサコ", "フミカ", "フラワ", "マウル", "マカナ",
        "マキビ", "マツノ", "マナミ", "マミ", "マモル", "マヤカ", "マユコ", "マリカ", "マワカ", "ミイ", "ミイト",
        "ミイナ", "ミエコ", "ミオ", "ミキア", "ミキヤ", "ミサエ", "ミサト", "ミシャ", "ミズキ", "ミツコ", "ミナエ",
        "ミナセ", "ミハル", "ミフミ", "ミマ", "ミユア", "ミュウ", "ミラ", "ミリア", "ミロ", "ムクノ", "ムル",
        "メグモ", "メグル", "メバエ", "メハナ", "モイ", "モネカ", "ユナ", "ユキ", "メルア", "ヤスコ", "ユアイ",
        "ユキコ", "ユキネ", "ユナギ", "ユララ", "ユリナ", "ヨウナ", "ヨシコ", "リカ", "リマホ", "リコ", "リナ",
        "リム", "リヨナ", "リンカ", "リンク", "リンネ", "リンリ", "ルラ", "ルリ", "ルリセ", "レイア", "レウ",
        "レイラ", "レイワ", "レスカ", "レリミ", "レンナ", "ロマ", "ワラビ"
    ]
}
FAMILY_NAMES_BLUEARCHIVE = {
    "生徒": [
        "西村", "山根", "馬場", "中嶋", "内藤", "飯塚", "岡田", "三浦", "安田", "武者小路", "岩本", "秋山", "宮川",
        "高野", "安達", "小野寺", "森山", "平野", "安藤", "宮田", "長谷川", "中川", "佐久間", "丸山", "池田", "入海",
        "岡崎", "高階", "河村", "堀毛", "吉宮", "菅原", "中水", "手倉森", "神佐", "八丈部", "石狩", "北村", "荒岡",
        "豊森", "比江山", "鶴衛", "國田", "竹幸", "對喜", "木露", "成田", "櫛間", "北垣", "松原", "武呂", "甲地",
        "久々津", "平山", "竹田", "阿志賀", "岸谷", "抜井", "前畑", "小笠原", "田島", "畠山", "名渕", "真楽", "榎澤",
        "天野", "禰覇", "星咲", "勇島", "荒木", "慶誾尼", "田口", "槇嶋", "菊池", "越路", "岡部", "橋添", "片山",
        "佐羽尾", "小里", "込山", "院去", "久宝寺", "西佐川", "奥田", "春日川", "阿座見野", "庄司", "神田", "武田",
        "笹氣", "万谷", "壁谷澤", "繁本", "豊見城", "瀧原", "上城", "谷開", "荒舩", "横田", "美々津", "岡村", "灰原",
        "河野", "大城", "葛原", "重信", "宮原", "鈴岡", "柴田", "為定", "一条橋", "伊関", "広住", "雲土", "来福",
        "東岡", "内田", "美談", "泡渕", "深溝", "門田", "峯林", "手銭", "砂金", "今地", "舛方", "日暮", "南塲",
        "槌井", "辻垣内", "中原", "新門", "東金", "荘田", "若有", "幌別", "児玉", "五百蔵", "貫地谷", "浦丸", "鳫島",
        "湯沢", "講堂", "鷲北", "金河", "尾崎", "印牧", "刀祢", "國松", "雉野", "石塚", "里永", "田ノ上", "組坂",
        "熊抱", "増淵", "岡本", "大野下", "宮崎", "四十萬谷", "五十嵐", "立福", "鷺沢", "盆子原", "荒井", "齋川",
        "嶋崎", "松子山", "市川", "能瀬", "蕨野", "在本", "米沢", "仲本", "一噌", "横山", "福岡", "宇智田", "神武",
        "津守", "宮城", "今村", "初取", "楽本", "福島", "釜野", "久我", "的之", "新金谷", "富田", "浜詰", "本間",
        "武野", "綾戸", "竹留", "木須井", "熊谷", "森本", "瀬古口", "半下石", "長尾", "玉ノ井", "細川", "三ツ扇",
        "追木", "那知", "橋森", "藤原", "窪井", "加茂前", "加谷", "河合", "木島", "東員", "上原", "高津戸", "原",
        "池嶌", "牛沢", "小島", "一守", "伊古田", "岩崎", "浅坂", "平柳", "中山", "受川", "辻", "苫名", "阿良田",
        "槐", "衣巻", "西幅", "遠松", "古座", "二通", "大崎", "稲恒", "大庄", "宝島", "坂口", "伊丹", "寺峰", "閨谷",
        "杉山", "樽川", "久城", "田辺", "村山"
    ]
}

# 能力値名リスト
STATUS_NAMES = [
    # 戦闘系能力値 (10個)
    "腕力", "耐久", "持久力", "敏捷", "照準力", "神秘総量", "神秘出力", "戦術眼", "統率", "車輛運転",
    # 一般系能力値 (10個)
    "学力", "機転", "政治力", "調理", "味覚", "芸術", "工作", "社交性", "魅力", "幸運"
]

EQUIPMENT_TYPES_BLUEARCHIVE = {
    "時計": "戦術眼", "カバン": "耐久", "靴": "敏捷", "ヘアピン": "照準力",
    "お守り": "幸運", "ネックレス": "神秘総量", "手袋": "神秘出力", "バッジ": "持久力"
}
EQUIPMENT_NAMES_BLUEARCHIVE = list(EQUIPMENT_TYPES_BLUEARCHIVE.keys())
ITEM_PREFIXES_BLUEARCHIVE = ["学園指定の", "ペロロ様印の", "サーバルの", "マナスルの", "ベロニカの",
                             "カゼヤマの", "ココデビルの", "トリプルステップの", "ローレライの", "ハルピュイアの"]

SCHOOLS_BLUEARCHIVE = {
    "連邦生徒会": 1,
    "アビドス高等学校": 1,
    "ゲヘナ学園": 2,
    "トリニティ総合学園": 2,
    "ミレニアムサイエンススクール": 2,
    "アリウス分校": 1,
    "百鬼夜行連合学院": 1,
    "山海経高級中学校": 1,
    "レッドウィンター連邦学園": 1,
    "ヴァルキューレ警察学校": 1,
    "SRT特殊学園": 1,
    "ハイランダー鉄道学園": 1,
    "ワイルドハント芸術学院": 1
}

ETHICS_MAP = {
    "強い秩序": lambda: random.randint(81, 100),
    "秩序": lambda: random.randint(61, 80),
    "中立": lambda: random.randint(40, 60),
    "混沌": lambda: random.randint(20, 39),
    "強い混沌": lambda: random.randint(0, 19),
}

MORALITY_MAP = {
    "高潔": lambda: random.randint(81, 100),
    "善": lambda: random.randint(61, 80),
    "中庸": lambda: random.randint(40, 60),
    "悪": lambda: random.randint(20, 39),
    "邪悪": lambda: random.randint(0, 19),
}

VALID_AGES = [15, 16, 17]


def generate_normal_value(mu, sigma, min_val, max_val):
    temp_value = random.normalvariate(mu, sigma)
    return max(min_val, min(max_val, round(temp_value)))


def generate_statuses_for_student(status_names_list, base_mu=50, base_sigma=19.4):
    if not status_names_list:
        return {}
    statuses = {}
    high_status_abilities = []
    for name in status_names_list:
        init_value = generate_normal_value(base_mu, base_sigma, 0, 100)
        statuses[name] = int(init_value)
        if statuses[name] >= 91:
            high_status_abilities.append(name)

    num_high_statuses = len(high_status_abilities)
    if num_high_statuses == 0:
        if status_names_list:
            eligible_statuses_for_talent = list(statuses.keys())
            if eligible_statuses_for_talent:
                status_to_enhance = random.choice(eligible_statuses_for_talent)
                statuses[status_to_enhance] = random.randint(91, 100)
    elif num_high_statuses > 1:
        talent_to_keep = random.choice(high_status_abilities)
        for name_to_adjust in high_status_abilities:
            if name_to_adjust != talent_to_keep:
                sigma_for_normal_degrade = base_sigma * 0.9
                adjusted_value = generate_normal_value(45, sigma_for_normal_degrade, 0, 90)
                statuses[name_to_adjust] = int(adjusted_value)
    return statuses


def generate_student_raw_data(affiliation_choice=None, ethics_choice=None, morality_choice=None, age_choice=None):
    """生徒の基本データを生成する。所属、倫理観、道徳観、年齢を指定可能。"""
    first_name = random.choice(FIRST_NAMES_BLUEARCHIVE[PLACEHOLDER_RACE_FOR_NAME])
    family_name = random.choice(FAMILY_NAMES_BLUEARCHIVE[PLACEHOLDER_RACE_FOR_NAME])
    name = f"{family_name} {first_name}"

    # 年齢の決定
    if age_choice is not None and age_choice in VALID_AGES:
        age = age_choice
    else:  # ランダムまたは不正な選択の場合、ランダムで決定
        age = random.randint(BLUEARCHIVE_AGE_MIN, BLUEARCHIVE_AGE_MAX)

    height = round(random.normalvariate(158, 8))
    height = max(130, min(180, height))

    if affiliation_choice and affiliation_choice in SCHOOLS_BLUEARCHIVE:
        affiliation = affiliation_choice
    else:
        weighted_schools = []
        for school, weight in SCHOOLS_BLUEARCHIVE.items():
            weighted_schools.extend([school] * weight)
        affiliation = random.choice(weighted_schools)

    if ethics_choice and ethics_choice in ETHICS_MAP:
        ethics = ETHICS_MAP[ethics_choice]()
    else:
        ethics = generate_normal_value(50, 19.4, 0, 100)

    if morality_choice and morality_choice in MORALITY_MAP:
        morality = MORALITY_MAP[morality_choice]()
    else:
        morality = generate_normal_value(50, 19.4, 0, 100)

    statuses = generate_statuses_for_student(STATUS_NAMES)

    item_type = random.choice(EQUIPMENT_NAMES_BLUEARCHIVE)
    item_prefix = random.choice(ITEM_PREFIXES_BLUEARCHIVE)
    equipment_name_str = f"{item_prefix}{item_type}"
    status_to_buff = EQUIPMENT_TYPES_BLUEARCHIVE[item_type]
    buff_amount = random.choice([2, 5, 10])
    buffed_status_info_str = f"{status_to_buff} +{buff_amount}"
    equipment_info = {"name": equipment_name_str, "type": item_type, "buffed_status_info": buffed_status_info_str}

    combat_status_total = sum(statuses[s] for s in STATUS_NAMES[:10])
    general_status_total = sum(statuses[s] for s in STATUS_NAMES[10:])

    return {
        "name": name,
        "affiliation": affiliation,
        "gender": "女性",
        "age": age,
        "height": height,
        "statuses": statuses,
        "equipment_name": equipment_name_str,
        "equipment_info": equipment_info,
        "combat_status_total": combat_status_total,
        "general_status_total": general_status_total,
        "ethics": ethics,
        "morality": morality,
    }


def get_alignment_name(ethics, morality):
    if ethics <= 19:
        eth_label = "強い混沌"
    elif ethics <= 39:
        eth_label = "混沌"
    elif ethics <= 60:
        eth_label = "中立"
    elif ethics <= 80:
        eth_label = "秩序"
    else:
        eth_label = "強い秩序"

    if morality <= 19:
        mor_label = "邪悪"
    elif morality <= 39:
        mor_label = "悪"
    elif morality <= 60:
        mor_label = "中庸"
    elif morality <= 80:
        mor_label = "善"
    else:
        mor_label = "高潔"

    return f"{eth_label}にして{mor_label}"


def create_help_text(options_list, unit=""):
    """選択肢のリストからヘルプ文字列を生成する"""
    text = "0: ランダム, "
    text += ", ".join([f"{i + 1}: {option}{unit}" for i, option in enumerate(options_list)])
    return text


def display_student(s_data):
    """生成された生徒データをコンソールに表示する"""
    print("\n--- 生成された生徒データ ---")
    print(f"名前: {s_data['name']}")
    print(f"所属: {s_data['affiliation']}")
    print(f"年齢: {s_data['age']}歳")
    print(f"身長: {s_data['height']}cm")

    alignment_display_name = get_alignment_name(s_data['ethics'], s_data['morality'])
    print(f"アライメント区分: {alignment_display_name} (倫理観: {s_data['ethics']}, 道徳観: {s_data['morality']})")

    print("\n全能力値リスト:")
    status_chunks = []
    current_chunk = []
    for i, status_name in enumerate(STATUS_NAMES):
        value = s_data['statuses'][status_name]
        display_value = str(value)
        if value >= 80:
            display_value = f"**{value}**"
        elif value <= 20:
            display_value = f"*{value}*"
        current_chunk.append(f"{status_name}: {display_value}")
        if (i + 1) % 10 == 0 or (i + 1) == len(STATUS_NAMES):
            status_chunks.append(", ".join(current_chunk))
            current_chunk = []
    for chunk in status_chunks:
        print(chunk)

    print(f"戦闘ステータス合計: {s_data['combat_status_total']}")
    print(f"一般ステータス合計: {s_data['general_status_total']}")
    print(f"装備: {s_data['equipment_name']}")
    if s_data['equipment_info']:
        print(f"  (種類: {s_data['equipment_info']['type']}, 詳細: {s_data['equipment_info']['buffed_status_info']})")


def get_user_choice(prompt, options, allow_random=True, random_text="ランダム"):
    """ユーザーに選択肢を提示し、入力を受け付ける関数"""
    print(f"\n{prompt}")
    # 倫理観と道徳観の選択肢を定義順に表示するためのソート
    if "強い秩序" in options:
        options = ["強い秩序", "秩序", "中立", "混沌", "強い混沌"]
    elif "高潔" in options:
        options = ["高潔", "善", "中庸", "悪", "邪悪"]

    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    if allow_random:
        print(f"{len(options) + 1}. {random_text}")

    while True:
        try:
            choice_input = input(f"選択してください (1-{len(options) + (1 if allow_random else 0)}): ")
            if not choice_input and allow_random:
                return "ランダム"

            choice_num = int(choice_input)
            if 1 <= choice_num <= len(options):
                return options[choice_num - 1]
            elif allow_random and choice_num == len(options) + 1:
                return "ランダム"
            else:
                print("無効な選択です。")
        except (ValueError, IndexError):
            print("無効な入力です。もう一度入力してください。")


def run_interactive_mode():
    """対話形式で生徒データを生成する"""
    print("キヴォトス生徒データジェネレーター")
    print("=" * 30)

    params = {
        "affiliation_choice": None,
        "ethics_choice": None,
        "morality_choice": None,
        "age_choice": None
    }

    choice_mode = get_user_choice("生成方法を選択してください:", ["何も指定しない完全ランダム", "個別に指定する"],
                                  allow_random=False)

    if choice_mode == "個別に指定する":
        school_list = list(SCHOOLS_BLUEARCHIVE.keys())
        chosen_affiliation = get_user_choice("--- 所属を選択してください ---", school_list,
                                             random_text="ランダムな所属")
        if chosen_affiliation != "ランダム":
            params["affiliation_choice"] = chosen_affiliation

        age_options_display = [f"{age}歳" for age in VALID_AGES]
        chosen_age_str = get_user_choice("--- 年齢を選択してください ---", age_options_display,
                                         random_text="ランダムな年齢")
        if chosen_age_str != "ランダム":
            params["age_choice"] = int(chosen_age_str.replace('歳', ''))

        ethics_options = list(ETHICS_MAP.keys())
        chosen_ethics = get_user_choice("--- 倫理観を選択してください ---", ethics_options,
                                        random_text="ランダムな倫理観")
        if chosen_ethics != "ランダム":
            params["ethics_choice"] = chosen_ethics

        morality_options = list(MORALITY_MAP.keys())
        chosen_morality = get_user_choice("--- 道徳観を選択してください ---", morality_options,
                                          random_text="ランダムな道徳観")
        if chosen_morality != "ランダム":
            params["morality_choice"] = chosen_morality
    else:
        print("\n完全ランダムで生徒を生成します。")

    s_data = generate_student_raw_data(**params)
    display_student(s_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ブルーアーカイブ風の生徒キャラクターを生成します。\n引数なしで実行すると対話モードになります。',
        formatter_class=argparse.RawTextHelpFormatter
    )

    school_list = list(SCHOOLS_BLUEARCHIVE.keys())
    # 定義順に並べ替える
    ethics_list = ["強い秩序", "秩序", "中立", "混沌", "強い混沌"]
    morality_list = ["高潔", "善", "中庸", "悪", "邪悪"]

    affiliation_help = create_help_text(school_list)
    age_help = create_help_text(VALID_AGES, unit="歳")
    ethics_help = create_help_text(ethics_list)
    morality_help = create_help_text(morality_list)

    parser.add_argument('--affiliation', help=f'所属学園を数値で指定:\n  {affiliation_help}', type=int,
                        choices=range(0, len(school_list) + 1))
    parser.add_argument('--age', help=f'年齢を数値で指定:\n  {age_help}', type=int,
                        choices=range(0, len(VALID_AGES) + 1))
    parser.add_argument('--ethics', help=f'倫理観を数値で指定:\n  {ethics_help}', type=int,
                        choices=range(0, len(ethics_list) + 1))
    parser.add_argument('--morality', help=f'道徳観を数値で指定:\n  {morality_help}', type=int,
                        choices=range(0, len(morality_list) + 1))

    if len(sys.argv) == 1:
        run_interactive_mode()
    else:
        args = parser.parse_args()

        affiliation_choice = school_list[args.affiliation - 1] if args.affiliation else None
        age_choice = VALID_AGES[args.age - 1] if args.age else None
        ethics_choice = ethics_list[args.ethics - 1] if args.ethics else None
        morality_choice = morality_list[args.morality - 1] if args.morality else None

        params = {
            "affiliation_choice": affiliation_choice,
            "age_choice": age_choice,
            "ethics_choice": ethics_choice,
            "morality_choice": morality_choice,
        }

        print("\n--- 引数に基づいて生徒を生成中 ---")
        student_data = generate_student_raw_data(**params)

        display_student(student_data)
