import pandas as pd
import random
import argparse
import sys
from datetime import datetime, timedelta
import subprocess # 追加: subprocessモジュールをインポート

# --- ウマ娘データ定義 ---

# 年齢
UMAMUSUME_AGE_MIN = 12
UMAMUSUME_AGE_MAX = 16

# ステータス
STATUS_NAMES_UMAMUSUME = ["スピード", "スタミナ", "パワー", "根性", "賢さ"]

# 適性
APTITUDE_RANKS = ["S", "A", "B", "C", "D", "E", "F", "G"]
TRACK_APTITUDES = ["芝", "ダート"]
DISTANCE_APTITUDES = ["短距離", "マイル", "中距離", "長距離"]
STRATEGY_APTITUDES = ["逃げ", "先行", "差し", "追込"]

# 性格
PERSONALITIES = ["熱血", "クール", "元気いっぱい", "おっとり", "真面目", "ミステリアス", "天然", "負けず嫌い"]

def generate_normal_value(mu, sigma, min_val, max_val):
    """正規分布に従う値を生成し、最小・最大値の範囲内に収める"""
    val = random.normalvariate(mu, sigma)
    return max(min_val, min(max_val, round(val)))

def generate_statuses(talented_status_pref=None):
    """ウマ娘の5つのステータスを生成する。得意ステータスの指定も可能。"""
    statuses = {}
    # ステータスの基準値。ゲームのBランクあたりを想定。
    base_mu = 700
    base_sigma = 200
    min_val = 500
    max_val = 1200

    for name in STATUS_NAMES_UMAMUSUME:
        statuses[name] = generate_normal_value(base_mu, base_sigma, min_val, max_val)

    # 指定された得意ステータスがあれば、その値を高くする
    if talented_status_pref and talented_status_pref in STATUS_NAMES_UMAMUSUME:
        # Sランク以上の高い値を保証
        statuses[talented_status_pref] = generate_normal_value(1100, 50, 1000, max_val)

    return statuses

def generate_aptitudes(track_pref=None, distance_pref=None, strategy_pref=None):
    """バ場、距離、脚質の適性を生成する。好みも反映可能。
       A・Sが一つもない場合はランダムに一つA・Sにする。
    """
    aptitudes = {"バ場": {}, "距離": {}, "脚質": {}}
    rank_weights = [1, 5, 20, 40, 20, 5, 2, 1]  # B,C,Dが出やすい

    # バ場適性
    # ユーザーが指定したバ場適性をS/Aにする
    if track_pref and track_pref in TRACK_APTITUDES:
        for track in TRACK_APTITUDES:
            if track == track_pref:
                aptitudes["バ場"][track] = random.choice(["S", "A"])
            else:
                aptitudes["バ場"][track] = random.choices(APTITUDE_RANKS, weights=rank_weights, k=1)[0]
    else: # 指定がない場合はランダムに生成
        for track in TRACK_APTITUDES:
            aptitudes["バ場"][track] = random.choices(APTITUDE_RANKS, weights=rank_weights, k=1)[0]
        
        # バ場適性でS/Aがない場合、ランダムに1つをS/Aにする
        if not any(aptitudes["バ場"][track] in ["S", "A"] for track in TRACK_APTITUDES):
            target_track = random.choice(TRACK_APTITUDES)
            aptitudes["バ場"][target_track] = random.choice(["S", "A"])

    # 距離適性
    dist_apts = {}
    for dist in DISTANCE_APTITUDES:
        dist_apts[dist] = random.choices(APTITUDE_RANKS, weights=rank_weights, k=1)[0]
    main_distance = distance_pref if distance_pref else random.choice(DISTANCE_APTITUDES)
    dist_apts[main_distance] = random.choice(["S", "A"])
    aptitudes["距離"] = dist_apts

    # 距離適性でS/Aがない場合、ランダムに1つをS/Aにする
    if not any(aptitudes["距離"][dist] in ["S", "A"] for dist in DISTANCE_APTITUDES):
        target_dist = random.choice(DISTANCE_APTITUDES)
        aptitudes["距離"][target_dist] = random.choice(["S", "A"])

    # 脚質適性
    strat_apts = {}
    for strat in STRATEGY_APTITUDES:
        strat_apts[strat] = random.choices(APTITUDE_RANKS, weights=rank_weights, k=1)[0]
    main_strategy = strategy_pref if strategy_pref else random.choice(STRATEGY_APTITUDES)
    strat_apts[main_strategy] = random.choice(["S", "A"])
    aptitudes["脚質"] = strat_apts

    # 脚質適性でS/Aがない場合、ランダムに1つをS/Aにする
    if not any(aptitudes["脚質"][strat] in ["S", "A"] for strat in STRATEGY_APTITUDES):
        target_strat = random.choice(STRATEGY_APTITUDES)
        aptitudes["脚質"][target_strat] = random.choice(["S", "A"])

    return aptitudes

def generate_umamusume_raw_data(track_pref=None, distance_pref=None, strategy_pref=None, personality_choice=None, age_choice=None, talented_status_pref=None):
    """一人のウマ娘の全データを生成する"""

    # Specify the path to the CSV file in Google Drive
    csv_file_path = '/content/drive/MyDrive/MobUmaNameList.csv'

    random_name = "名無しのウマ娘" # Default name in case of file error

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Check if the DataFrame is empty
        if not df.empty:
            # Select a random row (and thus a random name) from the DataFrame
            random_name = df.sample(n=1).iloc[0, 0] # Assuming the names are in the first column
        else:
            print("ファイルが空です。")

    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません: {csv_file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    
    age = age_choice if age_choice else random.randint(UMAMUSUME_AGE_MIN, UMAMUSUME_AGE_MAX)

    # 身長・スリーサイズ (年齢に応じて調整)
    # 12歳を基準として、年齢が1歳上がるごとに平均値を少し上げる
    age_factor = (age - UMAMUSUME_AGE_MIN) * 2.0 # 1歳につき1.0cm増
    
    height_mu = 148 + age_factor
    bust_mu_factor = 0.50 + (age - UMAMUSUME_AGE_MIN) * 0.005 # 1歳につき0.005増加
    waist_mu_factor = 0.71 + (age - UMAMUSUME_AGE_MIN) * 0.002
    hip_mu_factor = 1.03 + (age - UMAMUSUME_AGE_MIN) * 0.003


    height = generate_normal_value(height_mu, 6, 145, 175)
    bust = height * random.uniform(bust_mu_factor - 0.02, bust_mu_factor + 0.02) # 範囲を微調整
    waist = bust * random.uniform(waist_mu_factor - 0.02, waist_mu_factor + 0.02)
    hip = bust * random.uniform(hip_mu_factor - 0.02, hip_mu_factor + 0.02)
    three_sizes = f"B{round(bust)}/W{round(waist)}/H{round(hip)}"

    # 誕生日 (実際の競走馬の誕生月傾向を反映)
    # 3,4月が最も多く、2,5月が次に多く、その他が少ない
    month_weights = {
        1: 1, 2: 5, 3: 10, 4: 10, 5: 5, 6: 1,
        7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1
    }
    
    chosen_month = random.choices(list(month_weights.keys()), weights=list(month_weights.values()), k=1)[0]
    
    # 選択された月の最終日を取得
    if chosen_month == 2:
        max_day = 28 # 閏年は考慮しない
    elif chosen_month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31
    
    chosen_day = random.randint(1, max_day)
    birthday = f"{chosen_month}月{chosen_day}日"


    personality = personality_choice if personality_choice else random.choice(PERSONALITIES)

    statuses = generate_statuses(talented_status_pref=talented_status_pref)
    aptitudes = generate_aptitudes(track_pref, distance_pref, strategy_pref)

    return {
        "name": random_name,
        "age": age,
        "birthday": birthday,
        "height": height,
        "three_sizes": three_sizes,
        "personality": personality,
        "statuses": statuses,
        "aptitudes": aptitudes,
        "status_total": sum(statuses.values()),
    }



def display_umamusume(u_data):
    """生成されたウマ娘データをコンソールに表示し、成長シミュレーターを呼び出す"""
    print("\n--- 生成されたウマ娘データ ---")
    print(f"名前: {u_data['name']}")
    print(f"年齢: {u_data['age']}歳")
    print(f"誕生日: {u_data['birthday']}")
    print(f"身長: {u_data['height']}cm")
    print(f"スリーサイズ: {u_data['three_sizes']}")
    print(f"性格: {u_data['personality']}")
    
    print("\n--- シニア期夏合宿後ステータス ---")
    status_text = []
    for name, value in u_data['statuses'].items():
        display_value = str(value)
        if value >= 1000:
            display_value = f"**{value}**"
        elif value <= 300:
            display_value = f"*{value}*"
        status_text.append(f"{name}: {display_value}")
    print(" | ".join(status_text))
    print(f"(合計値: {u_data['status_total']})")

    # umamusume_growth_simulator.py を呼び出す部分
    try:
        command = [sys.executable, 'drive/MyDrive/umamusume_growth_simulator.py']
        for status_name, value in u_data['statuses'].items():
            command.append(f'--{status_name}')
            command.append(str(value))

        # 変更点: capture_output=True と text=True を追加
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # 変更点: シミュレーターの出力をここで表示
        print(result.stdout)

    except FileNotFoundError:
        print("エラー: 'umamusume_growth_simulator.py' が見つかりません。同じディレクトリに存在することを確認してください。")
    except subprocess.CalledProcessError as e:
        print(f"エラー: 成長シミュレーターの実行に失敗しました: {e.stderr}") # エラー出力を表示
    except Exception as e:
        print(f"不明なエラーが発生しました: {e}")
    
    print("--- 適性 ---")
    apt = u_data['aptitudes']
    print(f"バ場: 芝 {apt['バ場']['芝']} / ダート {apt['バ場']['ダート']}")
    dist_apt = " | ".join([f"{k} {v}" for k, v in apt['距離'].items()])
    print(f"距離: {dist_apt}")
    strat_apt = " | ".join([f"{k} {v}" for k, v in apt['脚質'].items()])
    print(f"脚質: {strat_apt}")
    print("-" * 28 + "\n")


def get_user_choice(prompt, options, allow_random=True, random_text="ランダム"):
    """ユーザーに選択肢を提示し、入力を受け付ける"""
    print(f"\n{prompt}")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    if allow_random:
        print(f"0. {random_text} (または Enter)")

    while True:
        try:
            choice_input = input(f"番号を選択してください (0-{(len(options))}): ")
            if not choice_input and allow_random:
                return None
            choice_num = int(choice_input)
            if allow_random and choice_num == 0:
                return None
            if 1 <= choice_num <= len(options):
                return options[choice_num - 1]
            else:
                print("無効な選択です。")
        except (ValueError, IndexError):
            print("無効な入力です。もう一度入力してください。")


def run_interactive_mode():
    """対話形式でウマ娘データを生成する"""
    print("オリジナルウマ娘ジェネレーター")
    print("=" * 30)

    params = {
        "track_pref": None, # 新しい引数
        "distance_pref": None,
        "strategy_pref": None,
        "personality_choice": None,
        "age_choice": None,
        "talented_status_pref": None
    }

    if get_user_choice("生成方法を選択してください:", ["完全ランダム", "項目を指定して生成"], allow_random=False) == "項目を指定して生成":
        params["talented_status_pref"] = get_user_choice("--- 得意なステータスを選択してください ---", STATUS_NAMES_UMAMUSUME)
        params["track_pref"] = get_user_choice("--- 得意なバ場適性を選択してください ---", TRACK_APTITUDES) # 追加
        params["distance_pref"] = get_user_choice("--- 得意な距離を選択してください ---", DISTANCE_APTITUDES)
        params["strategy_pref"] = get_user_choice("--- 得意な脚質を選択してください ---", STRATEGY_APTITUDES)
        params["personality_choice"] = get_user_choice("--- 性格を選択してください ---", PERSONALITIES)
        
        age_options_display = [f"{age}歳" for age in range(UMAMUSUME_AGE_MIN, UMAMUSUME_AGE_MAX + 1)]
        chosen_age_str = get_user_choice("--- 年齢を選択してください ---", age_options_display)
        if chosen_age_str:
            params["age_choice"] = int(chosen_age_str.replace('歳', ''))

    else:
        print("\n完全ランダムでウマ娘を生成します。")

    u_data = generate_umamusume_raw_data(**params)
    display_umamusume(u_data)


def create_help_text(options_list):
    """選択肢のリストからヘルプ文字列を生成する"""
    text = "0: ランダム, "
    text += ", ".join([f"{i + 1}: {option}" for i, option in enumerate(options_list)])
    return text


def main():
    """メイン関数: 引数の処理と実行"""
    parser = argparse.ArgumentParser(
        description='オリジナルのウマ娘を生成します。\n引数なしで実行すると対話モードになります。',
        formatter_class=argparse.RawTextHelpFormatter
    )

    ages = list(range(UMAMUSUME_AGE_MIN, UMAMUSUME_AGE_MAX + 1))
    
    parser.add_argument('--talent', help=f'得意ステータスを数値で指定:\n  {create_help_text(STATUS_NAMES_UMAMUSUME)}', type=int, choices=range(0, len(STATUS_NAMES_UMAMUSUME) + 1))
    parser.add_argument('--track', help=f'得意バ場適性を数値で指定:\n  {create_help_text(TRACK_APTITUDES)}', type=int, choices=range(0, len(TRACK_APTITUDES) + 1))
    parser.add_argument('--distance', help=f'得意距離を数値で指定:\n  {create_help_text(DISTANCE_APTITUDES)}', type=int, choices=range(0, len(DISTANCE_APTITUDES) + 1))
    parser.add_argument('--strategy', help=f'得意脚質を数値で指定:\n  {create_help_text(STRATEGY_APTITUDES)}', type=int, choices=range(0, len(STRATEGY_APTITUDES) + 1))
    parser.add_argument('--personality', help=f'性格を数値で指定:\n  {create_help_text(PERSONALITIES)}', type=int, choices=range(0, len(PERSONALITIES) + 1))
    parser.add_argument('--age', help=f'年齢を数値で指定:\n  {create_help_text([f"{a}歳" for a in ages])}', type=int, choices=range(0, len(ages) + 1))

    if len(sys.argv) == 1:
        run_interactive_mode()
    else:
        args = parser.parse_args()
        
        params = {
            "talented_status_pref": STATUS_NAMES_UMAMUSUME[args.talent - 1] if args.talent else None,
            "track_pref": TRACK_APTITUDES[args.track - 1] if args.track else None,
            "distance_pref": DISTANCE_APTITUDES[args.distance - 1] if args.distance else None,
            "strategy_pref": STRATEGY_APTITUDES[args.strategy - 1] if args.strategy else None,
            "personality_choice": PERSONALITIES[args.personality - 1] if args.personality else None,
            "age_choice": ages[args.age - 1] if args.age else None,
        }

        print("\n--- 引数に基づいてウマ娘を生成中 ---")
        umamusume_data = generate_umamusume_raw_data(**params)
        display_umamusume(umamusume_data)


if __name__ == '__main__':
    main()