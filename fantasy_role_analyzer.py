from role_definitions import BASIC_ROLES_DATA, ALIGNMENT_CONDITIONS_MAP, ADVANCED_ROLES_DATA

# --- ヘルパー関数 ---
def _calculate_basic_role_aptitude(character_abilities, target_role_name):
    """
    指定された基本ロールの適性スコア（主要ステータスの平均値）を計算する。
    """
    if target_role_name not in BASIC_ROLES_DATA:
        return 0, {}

    role_info = BASIC_ROLES_DATA[target_role_name]
    primary_stats = role_info["primary_stats"]

    if not primary_stats:
        return 0, {}

    score_sum = 0
    relevant_stats_values = {}
    for stat_name in primary_stats:
        # ロール定義で指定された能力値をキャラクターが持っているか直接確認
        value = character_abilities.get(stat_name, 0)
        score_sum += value
        relevant_stats_values[stat_name] = value

    return score_sum / len(primary_stats), relevant_stats_values


def _check_alignment(character_ethics, character_morality, required_alignment_name):
    """キャラクターのアライメントが要求条件を満たすかチェックする。"""
    if required_alignment_name not in ALIGNMENT_CONDITIONS_MAP:
        return False

    condition = ALIGNMENT_CONDITIONS_MAP[required_alignment_name]
    ethics_ok = condition["ethics"][0] <= character_ethics <= condition["ethics"][1]
    morality_ok = condition["morality"][0] <= character_morality <= condition["morality"][1]
    return ethics_ok and morality_ok


# --- メインのメソッド群 ---

def suggest_combat_basic_roles(character_abilities):
    """
    戦闘系基本ロールの適性を主要ステータスの平均値で判定し、上位3つを提示する。
    入力: character_abilities (dict) - キャラクターの能力値
    出力: list of dict - 上位3つの戦闘系基本ロールの情報（概要を含む）
    """
    aptitudes = []
    for combat_role_name, role_data in BASIC_ROLES_DATA.items():
        if role_data["type"] == "戦闘系基本":
            score, details = _calculate_basic_role_aptitude(character_abilities, combat_role_name)
            if score > 0:
                aptitudes.append({
                    "name": combat_role_name,
                    "score": score,
                    "details": details,
                    "description": role_data.get("description", "概要なし")
                })

    sorted_aptitudes = sorted(aptitudes, key=lambda x: x["score"], reverse=True)
    return sorted_aptitudes[:3]


def suggest_general_basic_roles(character_abilities):
    """
    一般系基本ロールの適性を主要ステータスの平均値で判定し、上位3つを提示する。
    入力: character_abilities (dict) - キャラクターの能力値
    出力: list of dict - 上位3つの一般系基本ロールの情報（概要を含む）
    """
    aptitudes = []
    for general_role_name, role_data in BASIC_ROLES_DATA.items():
        if role_data["type"] == "一般系基本":
            score, details = _calculate_basic_role_aptitude(character_abilities, general_role_name)
            if score > 0:
                aptitudes.append({
                    "name": general_role_name,
                    "score": score,
                    "details": details,
                    "description": role_data.get("description", "概要なし")
                })

    sorted_aptitudes = sorted(aptitudes, key=lambda x: x["score"], reverse=True)
    return sorted_aptitudes[:3]


def get_eligible_advanced_roles(character_abilities, character_ethics, character_morality):
    """
    就任可能な派生ロール・特殊ロールをすべて提示する。
    入力:
        character_abilities (dict) - キャラクターの能力値
        character_ethics (int) - キャラクターの倫理観 (0-100)
        character_morality (int) - キャラクターの道徳観 (0-100)
    出力: list of dict - 就任可能な派生ロール・特殊ロールの情報（概要を含む）
    """
    eligible_roles = []

    for role_data in ADVANCED_ROLES_DATA:
        advanced_role_name = role_data["name"]
        role_type = role_data["type"]

        alignment_ok = _check_alignment(character_ethics, character_morality, role_data["alignment_name"])
        if not alignment_ok:
            continue

        is_eligible = False
        if role_type in ["戦闘系派生", "一般系派生"]:
            base_role_name = role_data["base_role_name"]
            if base_role_name not in BASIC_ROLES_DATA:
                continue

            base_role_primary_stats = BASIC_ROLES_DATA[base_role_name]["primary_stats"]
            specific_stat_name = role_data["specific_stat_name"]
            specific_stat_value_req = role_data["specific_stat_value_required"]

            # 条件A（専門特化型）
            base_stats_ok_a = all(character_abilities.get(stat, 0) >= 50 for stat in base_role_primary_stats)
            specific_stat_ok_a = character_abilities.get(specific_stat_name, 0) >= specific_stat_value_req
            if base_stats_ok_a and specific_stat_ok_a:
                is_eligible = True

            # 条件B（バランス型）
            if not is_eligible:
                stats_for_b_check = set(base_role_primary_stats + [specific_stat_name])
                if all(character_abilities.get(stat, 0) >= 65 for stat in stats_for_b_check):
                    is_eligible = True

        elif role_type == "特殊":
            specific_stats_req = role_data["specific_stats_all_required"]
            if all(character_abilities.get(stat, 0) >= req_val for stat, req_val in specific_stats_req.items()):
                is_eligible = True

        if is_eligible:
            eligible_roles.append({
                "name": advanced_role_name,
                "description": role_data.get("description", "概要なし")
            })

    return eligible_roles


# --- メイン処理 (テスト用) ---
if __name__ == "__main__":
    # サンプルキャラクターデータ（飛行/遊泳能力を持つキャラと、勇者適性を持つキャラを追加）
    sample_character_human = {
        "name": "リアナ", "ethics": 30, "morality": 75,
        "abilities": {
            "腕力": 60, "耐久": 55, "持久力": 65, "敏捷": 70, "照準力": 50, "魔力": 55,
            "魔法抵抗": 40, "信仰": 40, "統率": 45, "騎乗": 85, "学力": 50, "機転": 82,
            "政治力": 30, "調理": 40, "味覚": 50, "芸術": 60, "工作": 70,
            "社交性": 65, "魅力": 85, "幸運": 75
        }
    }
    sample_character_bird = {
        "name": "スカイ", "ethics": 70, "morality": 70,
        "abilities": {
            "腕力": 40, "耐久": 50, "持久力": 60, "敏捷": 85, "照準力": 80, "魔力": 30,
            "魔法抵抗": 40, "信仰": 50, "統率": 80, "飛行": 95,
            "学力": 50, "機転": 75, "政治力": 30, "調理": 60, "味覚": 70, "芸術": 80, "工作": 40,
            "社交性": 65, "魅力": 70, "幸運": 60
        }
    }
    sample_character_mermaid = {
        "name": "マリーナ", "ethics": 50, "morality": 80,
        "abilities": {
            "腕力": 45, "耐久": 55, "持久力": 50, "敏捷": 70, "照準力": 60, "魔力": 92,
            "魔法抵抗": 70, "信仰": 65, "統率": 50, "遊泳": 98,
            "学力": 70, "機転": 65, "政治力": 50, "調理": 75, "味覚": 80, "芸術": 85, "工作": 50,
            "社交性": 80, "魅力": 90, "幸運": 40
        }
    }
    sample_character_hero = {
        "name": "アーサー", "ethics": 90, "morality": 95, # 強い秩序かつ高潔
        "abilities": {
            "腕力": 75, "耐久": 70, "持久力": 80, "敏捷": 65, "照準力": 60, "魔力": 50,
            "魔法抵抗": 65, "信仰": 80, "統率": 78, "騎乗": 70,
            "学力": 60, "機転": 70, "政治力": 65, "調理": 40, "味覚": 50, "芸術": 55, "工作": 60,
            "社交性": 75, "魅力": 85, "幸運": 91
        }
    }

    characters_to_test = [sample_character_human, sample_character_bird, sample_character_mermaid, sample_character_hero]

    for char_data in characters_to_test:
        print(f"--- キャラクター: {char_data['name']} ---")
        print(f"アライメント: 倫理観 {char_data['ethics']}, 道徳観 {char_data['morality']}")

        print("\n[戦闘系基本ロール おすすめ]")
        suggested_combat = suggest_combat_basic_roles(char_data["abilities"])
        if suggested_combat:
            for role in suggested_combat:
                print(f"  - {role['name']} (スコア: {role['score']:.2f})")
                print(f"    詳細: {role['details']}")
                print(f"    概要: {role['description']}")
        else:
            print("  (なし)")


        print("\n[一般系基本ロール おすすめ]")
        suggested_general = suggest_general_basic_roles(char_data["abilities"])
        if suggested_general:
            for role in suggested_general:
                print(f"  - {role['name']} (スコア: {role['score']:.2f})")
                print(f"    詳細: {role['details']}")
                print(f"    概要: {role['description']}")
        else:
            print("  (なし)")


        print("\n[就任可能な派生・特殊ロール]")
        eligible_advanced = get_eligible_advanced_roles(
            char_data["abilities"], char_data["ethics"], char_data["morality"]
        )
        if eligible_advanced:
            for role in eligible_advanced:
                print(f"  - {role['name']}")
                print(f"    概要: {role['description']}")
        else:
            print("  (なし)")
        print("\n" + "="*40 + "\n")
