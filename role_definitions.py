# 基本ロールの主要ステータスと役割概要定義
# (戦闘系17種、一般系17種)
BASIC_ROLES_DATA = {
    # 戦闘系基本ロール
    "戦士": {"type": "戦闘系基本", "primary_stats": ["腕力", "持久力"],
             "description": "物理的な戦闘を得意とし、最前線で戦う。"
                            "武器の扱いに長け、頑健な肉体を持つ。"},
    "騎士": {"type": "戦闘系基本", "primary_stats": ["腕力", "統率", "騎乗"],
             "description": "高い戦闘技術に加え、味方を率いる能力や馬術も持つ。"
                            "名誉や規律を重んじることが多い。"},
    "弓兵": {"type": "戦闘系基本", "primary_stats": ["照準力", "敏捷"],
             "description": "弓矢などの射撃武器を用いて、遠距離から正確な攻撃を行う。"
                            "機敏な動きで有利な位置を確保する。"},
    "斥候": {"type": "戦闘系基本", "primary_stats": ["敏捷", "機転"],
             "description": "隠密行動、偵察、罠の発見・解除などを行う。"
                            "軽装で、素早い判断力と行動力が求められる。"},
    "魔術師": {"type": "戦闘系基本", "primary_stats": ["魔力", "学力"],
               "description": "元素魔法、精神魔法など、様々な魔法を駆使して攻撃や支援を行う。"
                              "魔法の知識や理解度が重要。"},
    "僧侶": {"type": "戦闘系基本", "primary_stats": ["信仰", "魔力"],
             "description": "神聖な力や信仰に基づいた魔法（回復、防御、対アンデッドなど）を用いる。"
                            "精神的な支柱となることも。"},
    "格闘家": {"type": "戦闘系基本", "primary_stats": ["腕力", "敏捷", "持久力"],
               "description": "武器に頼らず、鍛え上げた肉体と打撃・組技で戦う。"
                              "素早い動きと強力な一撃を特徴とする。"},
    "盾役": {"type": "戦闘系基本", "primary_stats": ["耐久", "持久力", "魔法抵抗"],
             "description": "高い防御力と体力で敵の攻撃を引きつけ、味方を守ることに特化した役割。"},
    "遊撃兵": {"type": "戦闘系基本", "primary_stats": ["敏捷", "腕力", "機転"],
               "description": "高い機動力を活かし、敵陣をかく乱したり、側面や背後から奇襲をかけたりする。"},
    "僧兵": {"type": "戦闘系基本", "primary_stats": ["信仰", "腕力", "耐久"],
             "description": "信仰の力と武術を組み合わせて戦う兵士。"
                            "自己鍛錬と戒律を重んじ、神聖な力で自らを強化したりする。"},
    "指揮官": {"type": "戦闘系基本", "primary_stats": ["統率", "機転", "魅力"],
               "description": "戦場で部隊を指揮し、戦術を立案・実行する。"
                              "兵士の士気を高め、戦局を有利に導く。"},
    "工兵": {"type": "戦闘系基本", "primary_stats": ["耐久", "持久力", "工作"],
             "description": "戦場において陣地の設営、障害物の破壊、罠の設置など、戦闘支援のための工作活動を専門とする。"},
    "魔法剣士": {"type": "戦闘系基本", "primary_stats": ["腕力", "魔力", "敏捷"],
                 "description": "剣技と魔法の双方を扱い、武器に魔法効果を付与したり、魔法と剣術を織り交ぜた戦術を得意とする。"},
    "魔弓士": {"type": "戦闘系基本", "primary_stats": ["照準力", "魔力", "敏捷"],
               "description": "弓矢の扱いに長け、矢に様々な魔法効果を込めて放つ。"
                              "遠距離からの魔法的支援攻撃や精密な魔法射撃を行う。"},
    "投擲兵": {"type": "戦闘系基本", "primary_stats": ["照準力", "機転"],
               "description": "ナイフ、斧、手槍、爆弾などの投擲武器の扱いに長ける。"
                              "正確な投擲技術と状況判断力が求められる。"},
    "天翔兵": {"type": "戦闘系基本", "primary_stats": ["飛行", "敏捷", "照準力"],
               "description": "翼や飛行能力を駆使して大空を舞い、空中からの奇襲や高速の偵察を得意とする兵士。"
                              "その立体的な機動力は、地上の敵にとって大きな脅威となる。"},
    "妖歌の槍士": {"type": "戦闘系基本", "primary_stats": ["遊泳", "魔力", "敏捷"],
                   "description": "水の魔力を槍に乗せ、三次元的な水中機動で敵を翻弄する海の魔法戦士。"
                                  "その歌声は敵を惑わし、味方を鼓舞する力も持つ。"},

    # 一般系基本ロール
    "学者": {"type": "一般系基本", "primary_stats": ["学力", "機転"],
             "description": "様々な分野の知識を探求し、研究、分析、記録、教育などを行う。"},
    "農耕家": {"type": "一般系基本", "primary_stats": ["持久力", "腕力"],
               "description": "土地を耕し、作物を育てたり家畜を世話したりして食料を生産する。"
                              "自然の知識や忍耐力が求められる。"},
    "料理人": {"type": "一般系基本", "primary_stats": ["調理", "味覚"],
               "description": "食材の知識と調理技術を駆使して、美味しく栄養のある料理を提供する。"},
    "商人": {"type": "一般系基本", "primary_stats": ["政治力", "社交性", "機転"],
             "description": "商品の売買、交渉、流通などを通じて利益を上げる。"
                            "市場の動向を読む洞察力や交渉術が重要。"},
    "技術者": {"type": "一般系基本", "primary_stats": ["工作", "学力", "機転"],
               "description": "道具、機械、建築物などの設計や製作、修理を行う。"
                              "手先の器用さや専門知識が求められる。"},
    "芸術家": {"type": "一般系基本", "primary_stats": ["芸術", "魅力"],
               "description": "絵画、彫刻、音楽、詩作など、様々な形態の芸術作品を創造し、人々の心を豊かにする。"},
    "外交官": {"type": "一般系基本", "primary_stats": ["政治力", "社交性", "魅力"],
               "description": "国家や組織間の交渉、情報収集、友好関係の構築などを行う。"
                              "高いコミュニケーション能力と戦略的思考が求められる。"},
    "指導者": {"type": "一般系基本", "primary_stats": ["統率", "魅力", "政治力"],
               "description": "集団や組織を導き、目標達成に向けて人々をまとめ上げる。"
                              "決断力、カリスマ性、責任感が重要。"},
    "情報屋": {"type": "一般系基本", "primary_stats": ["機転", "社交性", "幸運"],
               "description": "様々な情報を収集、分析し、必要とする相手に提供する。"
                              "人脈や隠密行動のスキルも役立つ。"},
    "鑑定士": {"type": "一般系基本", "primary_stats": ["学力", "機転", "照準力"],
               "description": "物品（美術品、骨董品、魔法の品など）の真贋や価値を鋭い観察眼と豊富な知識で見極める専門家。"},
    "吟遊詩人": {"type": "一般系基本", "primary_stats": ["魅力", "芸術", "社交性"],
                 "description": "歌や演奏、物語の語り部として、人々に楽しみや感動、時には情報や教訓を伝える。"},
    "薬師": {"type": "一般系基本", "primary_stats": ["学力", "工作", "機転"],
             "description": "薬草や鉱物などから薬を調合・製造する専門家。"
                            "病の治療薬だけでなく、様々な効果を持つ薬品を扱う。"},
    "調教師": {"type": "一般系基本", "primary_stats": ["魅力", "統率", "持久力"],
               "description": "動物（馬、犬、鳥など）や、時には魔物や幻想生物を手懐け、訓練し、特定の目的のために使役する。"},
    "鍛冶屋": {"type": "一般系基本", "primary_stats": ["腕力", "持久力", "工作"],
               "description": "金属を加工し、武器、防具、農具、日用品など、様々な金属製品の製造や修理を行う職人。"},
    "占術師": {"type": "一般系基本", "primary_stats": ["機転", "魅力", "幸運"],
               "description": "様々な占術（星読み、カード、水晶玉など）を用いて未来を予見したり、運命に助言を与えたりする。"},
    "風の運び手": {"type": "一般系基本", "primary_stats": ["飛行", "持久力", "機転"],
                 "description": "飛行能力を活かし、山脈や海峡を越えて手紙や荷物を迅速に届ける配達人。"
                                "天候を読み、最短のルートを見つけ出す判断力も求められる。"},
    "海の探究者": {"type": "一般系基本", "primary_stats": ["遊泳", "学力", "魅力"],
                 "description": "広大な海の未知を求め、海底遺跡の調査や古代の海洋生物との交信を行う探検家兼学者。"
                                "その探究心とカリスマ性で、海の最も深い秘密に迫る。"},
}

# アライメント名と倫理観・道徳観の数値範囲のマッピング
ALIGNMENT_CONDITIONS_MAP = {
    "秩序にして善": {"ethics": (61, 100), "morality": (61, 100)},
    "中立にして善": {"ethics": (40, 60), "morality": (61, 100)},
    "混沌にして善": {"ethics": (0, 39), "morality": (61, 100)},
    "秩序にして中庸": {"ethics": (61, 100), "morality": (40, 60)},
    "真なる中立": {"ethics": (40, 60), "morality": (40, 60)},
    "混沌にして中庸": {"ethics": (0, 39), "morality": (40, 60)},
    "秩序にして悪": {"ethics": (61, 100), "morality": (0, 39)},
    "中立にして悪": {"ethics": (40, 60), "morality": (0, 39)},
    "混沌にして悪": {"ethics": (0, 40), "morality": (0, 39)},
    "強い秩序かつ高潔": {"ethics": (81, 100), "morality": (81, 100)},
    "強い混沌かつ邪悪": {"ethics": (0, 19), "morality": (0, 19)},
}

# 派生ロールと特殊ロールの定義データ
ADVANCED_ROLES_DATA = [
    # --- 戦闘系派生ロール (30種) ---
    # 1. 戦士ベース
    {"name": "反骨の勇士", "type": "戦闘系派生", "base_role_name": "戦士", "alignment_name": "混沌にして善",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "カリスマと不屈の闘志で民衆を導き、圧政に立ち向かう情熱的なリーダー。"},
    {"name": "圧制の先鋒", "type": "戦闘系派生", "base_role_name": "戦士", "alignment_name": "秩序にして悪",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "悪の君主に仕え、鉄の意志と統率力で秩序（圧制）を敷く冷酷な指揮官。"},
    # 2. 騎士ベース
    {"name": "聖騎士", "type": "戦闘系派生", "base_role_name": "騎士", "alignment_name": "秩序にして善",
     "specific_stat_name": "信仰", "specific_stat_value_required": 80,
     "description": "正義と秩序のため聖なる魔法を剣に宿し戦う騎士。"},
    {"name": "暗黒騎士", "type": "戦闘系派生", "base_role_name": "騎士", "alignment_name": "秩序にして悪",
     "specific_stat_name": "魔力", "specific_stat_value_required": 80,
     "description": "悪の君主に仕え、闇の力と恐怖で敵を支配する騎士。"},
    # 3. 弓兵ベース
    {"name": "義侠の猟師", "type": "戦闘系派生", "base_role_name": "弓兵", "alignment_name": "中立にして善",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "森と共に生き、卓越した弓術とカリスマで不正に苦しむ者を助ける自由な射手。"},
    {"name": "国境の監視官", "type": "戦闘系派生", "base_role_name": "弓兵", "alignment_name": "秩序にして中庸",
     "specific_stat_name": "持久力", "specific_stat_value_required": 80,
     "description": "国家の境界線を守る忍耐強く忠実な射手。正確無比な射撃で脅威を排除する。"},
    # 4. 斥候ベース
    {"name": "王国の隠密", "type": "戦闘系派生", "base_role_name": "斥候", "alignment_name": "秩序にして善",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "国家に忠誠を誓い、密偵網を指揮して王国の平和を影から守る諜報専門家。"},
    {"name": "情報の仲買人", "type": "戦闘系派生", "base_role_name": "斥候", "alignment_name": "真なる中立",
     "specific_stat_name": "学力", "specific_stat_value_required": 70,
     "description": "中立の立場で情報を収集・分析・取引する情報のエキスパート。"},
    # 5. 魔術師ベース
    {"name": "精霊の大魔道", "type": "戦闘系派生", "base_role_name": "魔術師", "alignment_name": "中立にして善",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "自然界の精霊と交感し、その叡智と力で世界の調和を護る魔術師。"},
    {"name": "大死霊術師", "type": "戦闘系派生", "base_role_name": "魔術師", "alignment_name": "中立にして悪",
     "specific_stat_name": "信仰", "specific_stat_value_required": 80,
     "description": "生と死の根源を探求し、禁断の死霊術を極め魂を操る魔術師。"},
    # 6. 僧侶ベース
    {"name": "異端の聖人", "type": "戦闘系派生", "base_role_name": "僧侶", "alignment_name": "混沌にして善",
     "specific_stat_name": "機転", "specific_stat_value_required": 80,
     "description": "既存の教義に囚われず、機転と奇跡で人々を救済する型破りな聖職者。"},
    {"name": "邪教の大神官", "type": "戦闘系派生", "base_role_name": "僧侶", "alignment_name": "秩序にして悪",
     "specific_stat_name": "政治力", "specific_stat_value_required": 80,
     "description": "邪教を率い、政治手腕で影響力を拡大し悪の秩序を確立しようとする指導者。"},
    # 7. 格闘家ベース
    {"name": "武道の宗師", "type": "戦闘系派生", "base_role_name": "格闘家", "alignment_name": "秩序にして善",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "心技体を極め、武の道を多くの弟子に伝え広める指導者。"},
    {"name": "狂乱の殺戮者", "type": "戦闘系派生", "base_role_name": "格闘家", "alignment_name": "混沌にして悪",
     "specific_stat_name": "芸術", "specific_stat_value_required": 80,
     "description": "破壊衝動と歪んだ美意識から、殺戮を芸術として行う恐怖の存在。"},
    # 8. 盾役ベース
    {"name": "守護騎士団長", "type": "戦闘系派生", "base_role_name": "盾役", "alignment_name": "秩序にして善",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "騎士団を率い、鉄壁の防衛線と絶対的な安心感を仲間に与える高潔な指揮官。"},
    {"name": "移動要塞", "type": "戦闘系派生", "base_role_name": "盾役", "alignment_name": "混沌にして中庸",
     "specific_stat_name": "敏捷", "specific_stat_value_required": 80,
     "description": "巨大な盾を軽々と操り、予測不能な動きで敵を翻弄し味方を護る型破りな守護者。"},
    # 9. 遊撃兵ベース
    {"name": "自由の疾風", "type": "戦闘系派生", "base_role_name": "遊撃兵", "alignment_name": "中立にして善",
     "specific_stat_name": "幸運", "specific_stat_value_required": 80,
     "description": "組織に縛られず、驚異的な幸運と機動力で弱者を助ける風のような遊撃兵。"},
    {"name": "悪徳領主の私兵", "type": "戦闘系派生", "base_role_name": "遊撃兵", "alignment_name": "秩序にして悪",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "悪徳領主に仕え、知略と隠密技術で主君の野望を影から支える遊撃兵。"},
    # 10. 僧兵ベース
    {"name": "戒律の鉄槌", "type": "戦闘系派生", "base_role_name": "僧兵", "alignment_name": "秩序にして中庸",
     "specific_stat_name": "魔法抵抗", "specific_stat_value_required": 80,
     "description": "教団の規律を絶対視し、異端を許さず鉄槌を下す法の番人。"},
    {"name": "破戒の遊行僧", "type": "戦闘系派生", "base_role_name": "僧兵", "alignment_name": "混沌にして中庸",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "自由奔放に各地を放浪し、型破りな言動と魅力で人々を導く（あるいは困惑させる）僧兵。"},
    # 11. 指揮官ベース
    {"name": "反乱軍の英雄", "type": "戦闘系派生", "base_role_name": "指揮官", "alignment_name": "混沌にして善",
     "specific_stat_name": "幸運", "specific_stat_value_required": 80,
     "description": "圧政に対し、カリスマと型破りな指揮、そして幸運で反乱軍を勝利に導く英雄。"},
    {"name": "汚職将軍", "type": "戦闘系派生", "base_role_name": "指揮官", "alignment_name": "中立にして悪",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "軍の指揮権を悪用し、その地位と知識で私腹を肥やす将軍。"},
    # 12. 工兵ベース
    {"name": "軍事工学の大家", "type": "戦闘系派生", "base_role_name": "工兵", "alignment_name": "秩序にして中庸",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "軍事技術としての工学を極め、兵器開発や陣地構築を研究・実践する専門家。"},
    {"name": "狂気の爆弾芸術家", "type": "戦闘系派生", "base_role_name": "工兵", "alignment_name": "混沌にして悪",
     "specific_stat_name": "芸術", "specific_stat_value_required": 80,
     "description": "破壊に歪んだ美意識を見出し、爆発物を芸術として無差別に恐怖をまき散らす危険人物。"},
    # 13. 魔法剣士ベース
    {"name": "魔法剣の賞金稼ぎ", "type": "戦闘系派生", "base_role_name": "魔法剣士", "alignment_name": "混沌にして中庸",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "スリルと報酬を求め、予測不能な戦いぶりと魅力で危険な依頼をこなす自由奔放な魔法剣士。"},
    {"name": "魂を喰らう魔剣士", "type": "戦闘系派生", "base_role_name": "魔法剣士", "alignment_name": "中立にして悪",
     "specific_stat_name": "信仰", "specific_stat_value_required": 80,
     "description": "倒した敵の魂を力に変える禁断の魔法剣を振るい、際限なく力を求める邪悪な剣士。"},
    # 14. 魔弓士ベース
    {"name": "反逆の魔弓", "type": "戦闘系派生", "base_role_name": "魔弓士", "alignment_name": "混沌にして善",
     "specific_stat_name": "機転", "specific_stat_value_required": 80,
     "description": "腐敗した権力に対し、卓越した機転と型破りな魔弓術で抵抗する自由の射手。"},
    {"name": "破滅の流星雨", "type": "戦闘系派生", "base_role_name": "魔弓士", "alignment_name": "混沌にして悪",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "世界への憎悪から終末的な魔法の矢を降らせ、歪んだカリスマで追随者を集める破壊者。"},
    # 15. 投擲兵ベース
    {"name": "十種競技の王者", "type": "戦闘系派生", "base_role_name": "投擲兵", "alignment_name": "真なる中立",
     "specific_stat_name": "敏捷", "specific_stat_value_required": 70,
     "description": "純粋に人間の身体能力の限界を追求し、走・跳・投のあらゆる能力を極めた万能のアスリート。"},
    {"name": "無差別爆弾テロリスト", "type": "戦闘系派生", "base_role_name": "投擲兵", "alignment_name": "混沌にして悪",
     "specific_stat_name": "工作", "specific_stat_value_required": 80,
     "description": "社会への憎悪から無差別に爆発物を投擲し、恐怖と混乱をまき散らす危険人物。"},
    # 16. 天翔兵ベース
    {"name": "竜巻の騎士", "type": "戦闘系派生", "base_role_name": "天翔兵", "alignment_name": "秩序にして善",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "卓越した飛行技術と戦術眼を併せ持ち、空の部隊を率いて戦うエリート騎士。"
                    "その機動力は戦場の流れを支配する。"},
    # 17. 妖歌の槍士ベース
    {"name": "深海の歌姫", "type": "戦闘系派生", "base_role_name": "妖歌の槍士", "alignment_name": "混沌にして悪",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "その歌声を破滅的な魔力へと昇華させた海の戦士。"
                    "美しい歌で船乗りを惑わし、敵を海の底へと引きずり込むことを愉しむ、恐るべき存在。"},

    # --- 一般系派生ロール (30種) ---
    # 1. 学者ベース
    {"name": "アカシックレコードの解読者", "type": "一般系派生", "base_role_name": "学者", "alignment_name": "真なる中立",
     "specific_stat_name": "幸運", "specific_stat_value_required": 70,
     "description": "宇宙のあらゆる情報が記録されたアカシックレコードの解読に挑む孤高の探求者。"},
    {"name": "マッドサイエンティスト", "type": "一般系派生", "base_role_name": "学者", "alignment_name": "混沌にして悪",
     "specific_stat_name": "工作", "specific_stat_value_required": 80,
     "description": "純粋な破壊衝動や歪んだ好奇心から、危険な発明品を生み出す科学者。"},
    # 2. 農耕家ベース
    {"name": "大荘園の管理人", "type": "一般系派生", "base_role_name": "農耕家", "alignment_name": "秩序にして中庸",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "広大な荘園の農業全般を厳格な規律と計画に基づいて管理・運営する専門家。"},
    {"name": "植物革命家", "type": "一般系派生", "base_role_name": "農耕家", "alignment_name": "混沌にして中庸",
     "specific_stat_name": "機転", "specific_stat_value_required": 80,
     "description": "既存の農法や常識に挑戦し、奇抜な発想で作物改良や革新的栽培法を追求する異端児。"},
    # 3. 料理人ベース
    {"name": "宮廷料理長", "type": "一般系派生", "base_role_name": "料理人", "alignment_name": "秩序にして善",
     "specific_stat_name": "政治力", "specific_stat_value_required": 80,
     "description": "国家の威信をかけた宴席を預かり、食を通じて影響力を行使する料理の外交官。"},
    {"name": "味覚の探究者", "type": "一般系派生", "base_role_name": "料理人", "alignment_name": "真なる中立",
     "specific_stat_name": "学力", "specific_stat_value_required": 70,
     "description": "純粋に食の可能性、未知の食材、究極の味覚体験を学術的に探求する孤高の料理人兼研究者。"},
    # 4. 商人ベース
    {"name": "市民革命支援者", "type": "一般系派生", "base_role_name": "商人", "alignment_name": "混沌にして善",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "商才と人脈、カリスマを駆使して市民革命を資金面や物資面から支援する商人。"},
    {"name": "略奪商戦団提督", "type": "一般系派生", "base_role_name": "商人", "alignment_name": "混沌にして悪",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "無法者を率い、沿岸を略奪し他国に転売する海上の支配者。実質は海賊。"},
    # 5. 技術者ベース
    {"name": "旅する人道的発明家", "type": "一般系派生", "base_role_name": "技術者", "alignment_name": "中立にして善",
     "specific_stat_name": "魅力", "specific_stat_value_required": 80,
     "description": "卓越した技術と魅力で各地を旅し、人道的見地から発明品で人々を助ける。"},
    {"name": "闇市場の違法兵器職人", "type": "一般系派生", "base_role_name": "技術者", "alignment_name": "中立にして悪",
     "specific_stat_name": "魔力", "specific_stat_value_required": 80,
     "description": "法や倫理を無視し、危険な兵器や違法な装置を秘密裏に開発・製作し闇市場で売買する技術者。"},
    # 6. 芸術家ベース
    {"name": "諷刺劇作家", "type": "一般系派生", "base_role_name": "芸術家", "alignment_name": "混沌にして善",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "既存の権威や社会の不正を、鋭い知性と諷刺劇で巧みに批判する芸術家。"},
    {"name": "冒涜的芸術家", "type": "一般系派生", "base_role_name": "芸術家", "alignment_name": "混沌にして悪",
     "specific_stat_name": "魔力", "specific_stat_value_required": 80,
     "description": "神聖なものや道徳的規範を意図的に踏みにじる冒涜的な作品を創造し、社会に混乱と不快感をもたらす。"},
    # 7. 外交官ベース
    {"name": "国際法の守護者", "type": "一般系派生", "base_role_name": "外交官", "alignment_name": "秩序にして善",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "国際法や倫理観の遵守を訴え、正義に基づいた国際秩序の実現に尽力する外交官。"},
    {"name": "不平等条約の黒幕", "type": "一般系派生", "base_role_name": "外交官", "alignment_name": "秩序にして悪",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "法的知識を悪用し、他国を不利益な条約で縛り付け従属させる外交戦略の黒幕。"},
    # 8. 指導者ベース
    {"name": "賢帝", "type": "一般系派生", "base_role_name": "指導者", "alignment_name": "秩序にして善",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "深い学識と先見の明で国家を賢明に統治し、民に平和と繁栄をもたらす理想的君主。"},
    {"name": "侵略的独裁者", "type": "一般系派生", "base_role_name": "指導者", "alignment_name": "秩序にして悪",
     "specific_stat_name": "腕力", "specific_stat_value_required": 80,
     "description": "強大な武力を背景に周辺諸国への侵略を繰り返し、恐怖で民衆を支配する独裁者。"},
    # 9. 情報屋ベース
    {"name": "巨大書庫の司書", "type": "一般系派生", "base_role_name": "情報屋", "alignment_name": "秩序にして中庸",
     "specific_stat_name": "学力", "specific_stat_value_required": 80,
     "description": "膨大な知識が眠る巨大書庫の管理者にして、情報の秩序を守る番人。"},
    {"name": "裏社会の情報王", "type": "一般系派生", "base_role_name": "情報屋", "alignment_name": "中立にして悪",
     "specific_stat_name": "政治力", "specific_stat_value_required": 80,
     "description": "あらゆる秘密を金で売買し、裏社会に広大な情報網を築き上げた情報屋の頂点。"},
    # 10. 鑑定士ベース
    {"name": "鑑定ギルドの権威", "type": "一般系派生", "base_role_name": "鑑定士", "alignment_name": "秩序にして中庸",
     "specific_stat_name": "統率", "specific_stat_value_required": 80,
     "description": "鑑定ギルドで組織をまとめ上げ、鑑定基準の維持と後進育成に尽力する重鎮。"},
    {"name": "トレジャーハンター", "type": "一般系派生", "base_role_name": "鑑定士", "alignment_name": "混沌にして中庸",
     "specific_stat_name": "幸運", "specific_stat_value_required": 80,
     "description": "鑑定眼と強運を頼りに、世界各地で価値ある珍品や遺物を探し求める冒険的鑑定士。"},
    # 11. 吟遊詩人ベース
    {"name": "詩聖", "type": "一般系派生", "base_role_name": "吟遊詩人", "alignment_name": "中立にして善",
     "specific_stat_name": "信仰", "specific_stat_value_required": 80,
     "description": "俗事に囚われず、聖なる詩歌と音楽で人々に癒やしと希望を与える放浪の芸術家。"},
    {"name": "扇動音楽家", "type": "一般系派生", "base_role_name": "吟遊詩人", "alignment_name": "秩序にして悪",
     "specific_stat_name": "工作", "specific_stat_value_required": 80,
     "description": "芸術的才能と工作技術で大衆の感情を巧みに操り、特定の思想へと扇動する音楽家。"},
    # 12. 薬師ベース
    {"name": "旅する薬草治療師", "type": "一般系派生", "base_role_name": "薬師", "alignment_name": "中立にして善",
     "specific_stat_name": "持久力", "specific_stat_value_required": 80,
     "description": "卓越した薬草知識と調合技術、不屈の持久力で各地を巡り、病に苦しむ人々を癒やす献身的な治療家。"},
    {"name": "毒薬専門調合師", "type": "一般系派生", "base_role_name": "薬師", "alignment_name": "中立にして悪",
     "specific_stat_name": "政治力", "specific_stat_value_required": 80,
     "description": "薬学知識を毒薬調合に特化させ、政治力を駆使して裏社会で暗躍する専門家。"},
    # 13. 調教師ベース
    {"name": "過激な動物愛護家", "type": "一般系派生", "base_role_name": "調教師", "alignment_name": "混沌にして善",
     "specific_stat_name": "敏捷", "specific_stat_value_required": 80,
     "description": "虐げられた動物や魔法生物を解放するため、時に違法な破壊活動も行う情熱的な活動家。"},
    {"name": "魔獣軍団訓練総監", "type": "一般系派生", "base_role_name": "調教師", "alignment_name": "秩序にして悪",
     "specific_stat_name": "魔力", "specific_stat_value_required": 80,
     "description": "悪の軍団に仕え、強力な魔獣や幻想生物を組織的に調練し、恐るべき軍団を育成する最高責任者。"},
    # 14. 鍛冶屋ベース
    {"name": "聖剣鍛冶師", "type": "一般系派生", "base_role_name": "鍛冶屋", "alignment_name": "秩序にして善",
     "specific_stat_name": "信仰", "specific_stat_value_required": 80,
     "description": "篤い信仰心と卓越した技術で、邪を打ち破る聖なる武具を鍛え上げる職人。"},
    {"name": "気まぐれな天才鍛冶師", "type": "一般系派生", "base_role_name": "鍛冶屋", "alignment_name": "混沌にして中庸",
     "specific_stat_name": "機転", "specific_stat_value_required": 80,
     "description": "常識に囚われず、閃きと機転で奇抜で実験的な作品を生み出す天才肌の職人。"},
    # 15. 占術師ベース
    {"name": "星詠みの革命思想家", "type": "一般系派生", "base_role_name": "占術師", "alignment_name": "混沌にして善",
     "specific_stat_name": "信仰", "specific_stat_value_required": 80,
     "description": "星々や予言を読み解き、革命運動に理論的正当性と希望を与える思想家。"},
    {"name": "絶望の招来者", "type": "一般系派生", "base_role_name": "占術師", "alignment_name": "混沌にして悪",
     "specific_stat_name": "魔力", "specific_stat_value_required": 80,
     "description": "強大な魔力と歪んだ占術で人々の運命を捻じ曲げ、悲劇と絶望を招来する存在。"},
    # 16. 風の運び手ベース
    {"name": "自由の翼", "type": "一般系派生", "base_role_name": "風の運び手", "alignment_name": "混沌にして中庸",
     "specific_stat_name": "幸運", "specific_stat_value_required": 80,
     "description": "組織や国家に縛られず、風の吹くままに世界を翔ける自由な運び手。"
                    "その驚異的な幸運と飛行技術で、どんな困難な配達も（気分次第で）成し遂げてしまう。"},
    # 17. 海の探究者ベース
    {"name": "珊瑚の賢者", "type": "一般系派生", "base_role_name": "海の探究者", "alignment_name": "中立にして善",
     "specific_stat_name": "信仰", "specific_stat_value_required": 80,
     "description": "海底に広がる珊瑚の森に住まい、古代から続く海の叡智と歴史を守り伝える賢者。"
                    "海の生物たちの声を聞き、そのバランスを保つために力を尽くす。"},

    # --- 特殊ロール (2種) ---
    {"name": "勇者", "type": "特殊", "alignment_name": "強い秩序かつ高潔",
     "specific_stats_all_required": {"腕力": 70, "統率": 70, "魅力": 70, "幸運": 70},
     "description": "揺るぎない正義の心と高潔な魂で巨大な悪に立ち向かう、選ばれし光の体現者。"},
    {"name": "魔王", "type": "特殊", "alignment_name": "強い混沌かつ邪悪",
     "specific_stats_all_required": {"魔力": 70, "学力": 70, "機転": 70, "魅力": 70},
     "description": "世界に混沌と破壊をもたらすことを愉しみ、圧倒的な個の力で秩序を蹂躙する孤高の災厄。"},
]
