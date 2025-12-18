import random
import argparse
import sys

def calculate_previous_growth_status(current_statuses, decrease_amount, variability_range):
    """
    現在のステータスから指定された減少量とばらつきを考慮して、前の成長期のステータスを計算する。

    Args:
        current_statuses (dict): 現在の成長期のステータス（例: {"スピード": 800, ...}）。
        decrease_amount (int): 各ステータスから引かれる基本量。
        variability_range (tuple): ランダムなばらつきの範囲 (min_variability, max_variability)。

    Returns:
        dict: 計算された前の成長期のステータス。
    """
    previous_statuses = {}
    min_val, max_val = variability_range

    for status_name, value in current_statuses.items():
        # 基本値から減少量を引く
        base_reduced_value = value - decrease_amount
        
        # ランダムなばらつきを加える
        variability = random.randint(min_val, max_val)
        calculated_value = base_reduced_value + variability
        
        # ステータスは1未満にならないようにする
        previous_statuses[status_name] = max(1, calculated_value)
    
    return previous_statuses

def simulate_reverse_growth(senior_statuses):
    """
    シニア期のステータスから、クラシック期とジュニア期のステータスをシミュレートする。

    Args:
        senior_statuses (dict): シニア期のステータス。

    Returns:
        tuple: (junior_statuses, classic_statuses, senior_statuses) のタプル。
    """
    print("\n--- 逆算成長シミュレーション ---")

    # クラシック期のステータスを計算
    # シニア期より約200低い、ばらつき: -20 ~ +20
    classic_statuses = calculate_previous_growth_status(senior_statuses, 200, (-20, 20))
    print("\n--- クラシック期夏合宿後ステータス ---")
    print(" | ".join([f"{k}: {v}" for k, v in classic_statuses.items()]))

    # ジュニア期のステータスを計算
    # クラシック期より約200低い、ばらつき: -20 ~ +20
    junior_statuses = calculate_previous_growth_status(classic_statuses, 200, (-20, 20))
    print("\n--- ジュニア期デビュー時ステータス ---")
    print(" | ".join([f"{k}: {v}" for k, v in junior_statuses.items()]))

    return junior_statuses, classic_statuses, senior_statuses

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='シニア期のウマ娘ステータスから、クラシック期とジュニア期のステータスを逆算します。'
    )
    
    # 各ステータスの引数を追加
    parser.add_argument('--スピード', type=int, required=True, help='シニア期のスピード値を指定します。')
    parser.add_argument('--スタミナ', type=int, required=True, help='シニア期のスタミナ値を指定します。')
    parser.add_argument('--パワー', type=int, required=True, help='シニア期のパワー値を指定します。')
    parser.add_argument('--根性', type=int, required=True, help='シニア期の根性値を指定します。')
    parser.add_argument('--賢さ', type=int, required=True, help='シニア期の賢さ値を指定します。')

    args = parser.parse_args()

    senior_statuses_from_args = {
        "スピード": args.スピード,
        "スタミナ": args.スタミナ,
        "パワー": args.パワー,
        "根性": args.根性,
        "賢さ": args.賢さ
    }

    # シミュレーションを実行
    junior_stats, classic_stats, senior_stats = simulate_reverse_growth(senior_statuses_from_args)