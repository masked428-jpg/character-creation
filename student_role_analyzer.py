# coding: utf-8

# 能力値名リスト
STATUS_NAMES = [
    # 戦闘系能力値 (10個)
    "腕力", "耐久", "持久力", "敏捷", "照準力", "統率", "車輛運転", "神秘総量", "神秘出力", "戦術眼",
    # 一般系能力値 (10個)
    "学力", "機転", "政治力", "調理", "味覚", "芸術", "工作", "社交性", "魅力", "幸運"
]

# 戦闘ロール定義と適性能力値
COMBAT_ROLE_DEFINITIONS = {
    "アタッカー_FRONT": {"main_stats": ["腕力", "敏捷"], "sub_stats": ["耐久", "照準力"],
                         "position": "FRONT", "class": "アタッカー"},
    "アタッカー_MIDDLE": {"main_stats": ["照準力", "敏捷"], "sub_stats": ["腕力", "神秘出力"],
                          "position": "MIDDLE", "class": "アタッカー"},
    "アタッカー_BACK": {"main_stats": ["照準力", "戦術眼"], "sub_stats": ["神秘出力", "持久力"],
                        "position": "BACK", "class": "アタッカー"},
    "アタッカー_SPECIAL": {"main_stats": ["神秘出力", "照準力"], "sub_stats": ["戦術眼", "神秘総量", "統率"],
                           "position": "SPECIAL", "class": "アタッカー"},
    "タンク_FRONT": {"main_stats": ["耐久", "持久力"], "sub_stats": ["統率", "腕力"],
                     "position": "FRONT", "class": "タンク", "allowed_ethics": ["強い秩序", "秩序", "中立"]},
    "サポーター_MIDDLE": {"main_stats": ["統率", "神秘総量", "機転"], "sub_stats": ["耐久", "戦術眼", "神秘出力"],
                          "position": "MIDDLE", "class": "サポーター"},
    "サポーター_BACK": {"main_stats": ["統率", "神秘総量", "戦術眼"], "sub_stats": ["機転", "神秘出力"],
                        "position": "BACK", "class": "サポーター"},
    "サポーター_SPECIAL": {"main_stats": ["神秘総量", "統率", "戦術眼"], "sub_stats": ["神秘出力", "機転"],
                           "position": "SPECIAL", "class": "サポーター"},
    "ヒーラー_MIDDLE": {"main_stats": ["神秘総量", "神秘出力"], "sub_stats": ["耐久", "統率", "魅力"],
                        "position": "MIDDLE", "class": "ヒーラー", "allowed_morality": ["高潔", "善", "中庸"]},
    "ヒーラー_BACK": {"main_stats": ["神秘総量", "神秘出力"], "sub_stats": ["統率", "魅力"],
                      "position": "BACK", "class": "ヒーラー", "allowed_morality": ["高潔", "善", "中庸"]},
    "ヒーラー_SPECIAL": {"main_stats": ["神秘総量", "神秘出力", "統率"], "sub_stats": ["戦術眼", "魅力"],
                         "position": "SPECIAL", "class": "ヒーラー", "allowed_morality": ["高潔", "善", "中庸"]},
    "T.S._SPECIAL": {"main_stats": ["車輛運転", "照準力"], "sub_stats": ["統率", "工作", "戦術眼"],
                     "position": "SPECIAL", "class": "T.S."}
}

# 一般ロール定義と適性能力値
GENERAL_ROLE_DEFINITIONS = {
    "研究者/学者": {"main_stats": ["学力", "機転"], "sub_stats": ["工作", "幸運"]},
    "エンジニア/発明家": {"main_stats": ["工作", "学力"], "sub_stats": ["機転", "照準力"]},
    "戦術家/指揮官補佐": {"main_stats": ["戦術眼", "統率"], "sub_stats": ["機転", "政治力"],
                          "allowed_ethics": ["強い秩序", "秩序", "中立"]},
    "交渉人/情報収集家": {"main_stats": ["社交性", "機転"], "sub_stats": ["政治力", "魅力"]},
    "アーティスト/デザイナー": {"main_stats": ["芸術", "魅力"], "sub_stats": ["工作", "幸運"]},
    "料理研究家/パティシエ": {"main_stats": ["調理", "味覚"], "sub_stats": ["芸術", "機転"]},
    "アイドル/広報担当": {"main_stats": ["魅力", "社交性"], "sub_stats": ["芸術", "持久力"],
                          "allowed_morality": ["高潔", "善"]},
    "機械整備士/技師": {"main_stats": ["工作", "車輛運転"], "sub_stats": ["耐久", "学力"]},
    "カウンセラー/世話役": {"main_stats": ["魅力", "社交性"], "sub_stats": ["機転", "幸運"],
                            "allowed_ethics": ["強い秩序", "秩序", "中立"],
                            "allowed_morality": ["高潔", "善", "中庸"]},
    "探索家/トレジャーハンター": {"main_stats": ["幸運", "持久力", "敏捷"], "sub_stats": ["機転", "戦術眼"]},
    "ジャーナリスト/レポーター": {"main_stats": ["社交性", "機転", "学力"], "sub_stats": ["魅力", "幸運"]},
    "経営者/店舗運営者": {"main_stats": ["政治力", "社交性", "機転"], "sub_stats": ["幸運", "魅力"]}
}

# 火器種類定義と適性能力値
WEAPON_TYPE_DEFINITIONS = {
    "アサルトライフル(AR)": {"main_stats": ["照準力", "腕力"], "sub_stats": ["敏捷", "戦術眼"],
                             "notes": "汎用性が高い"},
    "サブマシンガン(SMG)": {"main_stats": ["敏捷", "照準力"], "sub_stats": ["腕力"],
                            "notes": "近～中距離、取り回し重視"},
    "スナイパーライフル(SR)": {"main_stats": ["照準力", "戦術眼"], "sub_stats": ["持久力", "幸運"],
                               "notes": "長距離精密射撃、腕力も若干影響"},
    "ショットガン(SG)": {"main_stats": ["腕力", "耐久"], "sub_stats": ["敏捷"],
                         "notes": "近距離高火力、照準力は低くても可"},
    "ハンドガン(HG)": {"main_stats": ["照準力", "敏捷"], "sub_stats": ["機転"],
                       "notes": "軽量で扱いやすい"},
    "マシンガン(MG)": {"main_stats": ["腕力", "持久力"], "sub_stats": ["照準力", "耐久"],
                       "notes": "制圧射撃、反動制御に腕力"},
    "グレネードランチャー(GL)": {"main_stats": ["工作", "腕力"], "sub_stats": ["戦術眼", "照準力"],
                                 "notes": "範囲攻撃、特殊弾も"},
    "レールガン(RG)/特殊粒子砲": {"main_stats": ["工作", "神秘出力"], "sub_stats": ["照準力", "神秘総量"],
                                  "notes": "技術力や神秘力が高い場合"},
    "火炎放射器(FT)": {"main_stats": ["持久力", "工作"], "sub_stats": ["腕力", "神秘出力"],
                       "notes": "近～中距離のエリア制圧"},
    "戦車": {"main_stats": ["車輛運転", "戦術眼", "照準力"], "sub_stats": ["統率", "工作", "耐久"],
             "notes": "搭乗・運用、高い判断力も要す"},
}


def calculate_role_score(student_statuses, role_definition, main_weight=3, sub_weight=1):
    """
    特定のロールに対する生徒の適性スコアを計算する。
    """
    score = 0
    for stat in role_definition["main_stats"]:
        score += student_statuses.get(stat, 0) * main_weight
    for stat in role_definition["sub_stats"]:
        score += student_statuses.get(stat, 0) * sub_weight
    return score


# 【新機能】倫理観・道徳観の数値からラベルを取得する関数群
def get_ethics_label(ethics):
    """
    5x5アライメント解説に基づき、倫理観の数値から対応するラベルを返す。
    """
    if ethics >= 81:
        return "強い秩序"
    elif ethics >= 61:
        return "秩序"
    elif ethics >= 40:
        return "中立"
    elif ethics >= 20:
        return "混沌"
    else:  # 0-19
        return "強い混沌"


def get_morality_label(morality):
    """
    5x5アライメント解説に基づき、道徳観の数値から対応するラベルを返す。
    """
    if morality >= 81:
        return "高潔"
    elif morality >= 61:
        return "善"
    elif morality >= 40:
        return "中庸"
    elif morality >= 20:
        return "悪"
    else:  # 0-19
        return "邪悪"


# 【変更点】 suggest_combat_roles に生徒の倫理観(student_ethics)を追加
def suggest_combat_roles(student_statuses, student_ethics, student_morality, num_suggestions=3):
    """
    生徒の能力値とアライメントに基づいておすすめの戦闘系ロールを提案する。
    """
    scores = []
    ethics_label = get_ethics_label(student_ethics)
    morality_label = get_morality_label(student_morality)

    for role_key, definition in COMBAT_ROLE_DEFINITIONS.items():
        score = calculate_role_score(student_statuses, definition)
        role_name = f"{definition['position']} / {definition['class']}"
        suitable = True

        # アライメントによるロール制限のチェック
        if "allowed_ethics" in definition and ethics_label not in definition["allowed_ethics"]:
            suitable = False
        if "allowed_morality" in definition and morality_label not in definition["allowed_morality"]:
            suitable = False

        if suitable:
            # 能力値による閾値チェック
            if definition["class"] == "タンク" and student_statuses.get("耐久", 0) < 55:
                suitable = False
            elif definition["class"] == "アタッカー" and definition["position"] == "BACK" and student_statuses.get(
                    "照準力", 0) < 65:
                suitable = False
            elif definition["class"] == "ヒーラー" and definition["position"] in ["MIDDLE",
                                                                                  "BACK"] and student_statuses.get(
                    "神秘出力", 0) < 40:
                suitable = False
            elif definition["class"] == "T.S." and (
                    student_statuses.get("車輛運転", 0) < 45 and student_statuses.get("工作", 0) < 45):
                suitable = False
            elif definition["class"] == "アタッカー" and definition["position"] == "SPECIAL" and (
                    student_statuses.get("神秘出力", 0) < 50 and student_statuses.get("照準力", 0) < 50):
                suitable = False
            elif definition["class"] == "サポーター" and definition["position"] == "SPECIAL" and (
                    student_statuses.get("神秘総量", 0) < 50 and student_statuses.get("統率", 0) < 40):
                suitable = False
            elif definition["class"] == "ヒーラー" and definition["position"] == "SPECIAL" and (
                    student_statuses.get("神秘総量", 0) < 50 and student_statuses.get("神秘出力", 0) < 45):
                suitable = False
            elif definition["position"] == "FRONT" and definition["class"] in ["サポーター", "ヒーラー"]:
                suitable = False

        if suitable:
            scores.append({"role_name": role_name, "score": score, "class": definition["class"],
                           "position": definition["position"]})

    # スコアの高い順にソート
    sorted_roles = sorted(scores, key=lambda x: x["score"], reverse=True)

    recommended_roles = []
    selected_classes = set()
    selected_positions_count = {"FRONT": 0, "MIDDLE": 0, "BACK": 0, "SPECIAL": 0}
    max_per_position = 2  # 同じ立ち位置からは最大2つまで（多様性のため）

    if sorted_roles:
        first_choice = sorted_roles[0]
        recommended_roles.append(first_choice["role_name"])
        selected_classes.add(first_choice["class"])
        selected_positions_count[first_choice["position"]] += 1

    for candidate in sorted_roles[1:]:
        if len(recommended_roles) >= num_suggestions:
            break
        if candidate["class"] not in selected_classes and \
                selected_positions_count.get(candidate["position"], 0) < max_per_position:
            recommended_roles.append(candidate["role_name"])
            selected_classes.add(candidate["class"])
            selected_positions_count[candidate["position"]] = selected_positions_count.get(candidate["position"], 0) + 1

    if len(recommended_roles) < num_suggestions:
        remaining_candidates = [r for r in sorted_roles if r["role_name"] not in recommended_roles]
        for candidate in remaining_candidates:
            if len(recommended_roles) >= num_suggestions:
                break
            if selected_positions_count.get(candidate["position"], 0) < max_per_position:
                recommended_roles.append(candidate["role_name"])
                selected_positions_count[candidate["position"]] = selected_positions_count.get(candidate["position"],
                                                                                               0) + 1
            elif len(recommended_roles) < num_suggestions:
                recommended_roles.append(candidate["role_name"])

    return recommended_roles[:num_suggestions]


# 【変更点】 suggest_general_roles に生徒の倫理観・道徳観を追加
def suggest_general_roles(student_statuses, student_ethics, student_morality, num_suggestions=3):
    """
    生徒の能力値とアライメントに基づいておすすめの一般系ロールを提案する。
    """
    scores = []
    ethics_label = get_ethics_label(student_ethics)
    morality_label = get_morality_label(student_morality)

    for role_name, definition in GENERAL_ROLE_DEFINITIONS.items():
        score = calculate_role_score(student_statuses, definition)
        suitable = True

        if "allowed_ethics" in definition and ethics_label not in definition["allowed_ethics"]:
            suitable = False
        if "allowed_morality" in definition and morality_label not in definition["allowed_morality"]:
            suitable = False

        if suitable:
            if role_name == "エンジニア/発明家" and student_statuses.get("工作", 0) < 60:
                suitable = False
            elif role_name == "研究者/学者" and student_statuses.get("学力", 0) < 60:
                suitable = False
            elif role_name == "アイドル/広報担当" and student_statuses.get("魅力", 0) < 50:
                suitable = False
            elif role_name == "ジャーナリスト/レポーター" and (
                    student_statuses.get("社交性", 0) < 50 or student_statuses.get("学力", 0) < 50):
                suitable = False
            elif role_name == "経営者/店舗運営者" and (
                    student_statuses.get("政治力", 0) < 50 or student_statuses.get("機転", 0) < 50):
                suitable = False

        if suitable:
            scores.append({"role_name": role_name, "score": score})

    # スコアの高い順にソート
    sorted_roles = sorted(scores, key=lambda x: x["score"], reverse=True)
    return [r["role_name"] for r in sorted_roles[:num_suggestions]]


def suggest_weapon_types(student_statuses, num_suggestions=3):
    """
    生徒の能力値に基づいておすすめの火器種類を提案する。
    """
    scores = []
    for weapon_name, definition in WEAPON_TYPE_DEFINITIONS.items():
        score = calculate_role_score(student_statuses, definition)
        suitable = True
        if weapon_name == "スナイパーライフル(SR)" and student_statuses.get("照準力", 0) < 60:
            suitable = False
        if weapon_name == "マシンガン(MG)" and student_statuses.get("腕力", 0) < 55:
            suitable = False
        if weapon_name == "ショットガン(SG)" and student_statuses.get("腕力", 0) < 45:
            suitable = False
        if weapon_name == "レールガン(RG)/特殊粒子砲" and student_statuses.get("工作", 0) < 70 and student_statuses.get(
                "神秘出力", 0) < 50:
            suitable = False
        if weapon_name == "火炎放射器(FT)" and student_statuses.get("持久力",0) < 55:
            suitable = False
        if weapon_name == "戦車" and (
                student_statuses.get("車輛運転", 0) < 70 or student_statuses.get("戦術眼", 0) < 50):
            suitable = False

        if suitable:
            scores.append({"weapon_name": weapon_name, "score": score, "notes": definition.get("notes", "")})

    # スコアの高い順にソート
    sorted_weapons = sorted(scores, key=lambda x: x["score"], reverse=True)

    recommended_weapons_with_notes = []
    selected_weapon_names = set()
    for weapon_info in sorted_weapons:
        if len(recommended_weapons_with_notes) < num_suggestions:
            if weapon_info["weapon_name"] not in selected_weapon_names:
                recommended_weapons_with_notes.append(f"{weapon_info['weapon_name']} ({weapon_info['notes']})")
                selected_weapon_names.add(weapon_info["weapon_name"])
    return recommended_weapons_with_notes[:num_suggestions]


if __name__ == '__main__':
    # テスト用の生徒データ
    student_data_list = [
        {
            "name": "テスト生徒A (混沌・悪)",
            "statuses": {"腕力": 80, "耐久": 80, "持久力": 80, "敏捷": 50, "照準力": 50, "統率": 20, "車輛運転": 20,
                         "神秘総量": 70, "神秘出力": 70, "戦術眼": 30, "学力": 40, "機転": 30, "政治力": 10, "調理": 10,
                         "味覚": 10, "芸術": 10, "工作": 10, "社交性": 10, "魅力": 90, "幸運": 50},
            "ethics": 10,  # 強い混沌
            "morality": 30  # 悪
        },
        {
            "name": "テスト生徒B (秩序・善)",
            "statuses": {"腕力": 50, "耐久": 80, "持久力": 80, "敏捷": 50, "照準力": 50, "統率": 80, "車輛運転": 20,
                         "神秘総量": 80, "神秘出力": 80, "戦術眼": 80, "学力": 70, "機転": 70, "政治力": 60, "調理": 50,
                         "味覚": 50, "芸術": 70, "工作": 30, "社交性": 90, "魅力": 90, "幸運": 70},
            "ethics": 70,  # 秩序
            "morality": 90  # 高潔
        }
    ]

    for student in student_data_list:
        print("=" * 30)
        print(f"生徒: {student['name']}")
        ethics_label = get_ethics_label(student['ethics'])
        morality_label = get_morality_label(student['morality'])
        print(
            f"アライメント: {ethics_label}・{morality_label} (倫理: {student['ethics']}, 道徳: {student['morality']})")

        print("\n--- おすすめ戦闘系ロール ---")
        recommended_combat_roles = suggest_combat_roles(student['statuses'], student['ethics'], student['morality'])
        if not recommended_combat_roles:
            print("適性のあるロールが見つかりませんでした。")
        for i, role in enumerate(recommended_combat_roles):
            print(f"{i + 1}. {role}")

        print("\n--- おすすめ一般系ロール ---")
        recommended_general_roles = suggest_general_roles(student['statuses'], student['ethics'], student['morality'])
        if not recommended_general_roles:
            print("適性のあるロールが見つかりませんでした。")
        for i, role in enumerate(recommended_general_roles):
            print(f"{i + 1}. {role}")

        print("\n--- おすすめ火器種類 ---")
        recommended_weapons = suggest_weapon_types(student['statuses'])
        if not recommended_weapons:
            print("適性のある火器が見つかりませんでした。")
        for i, weapon in enumerate(recommended_weapons):
            print(f"{i + 1}. {weapon}")
        print("=" * 30)
