from pyscript import document

def calculate(event):
    # 各入力値の取得
    try:
        wage = float(document.querySelector("#wage").value)
        hours = float(document.querySelector("#hours").value)
        break_h = float(document.querySelector("#break_hours").value)
        night_h = float(document.querySelector("#night_hours").value)
        trans = float(document.querySelector("#transport").value)

        # 実労働時間の計算（総時間 - 休憩）
        actual_hours = max(0, hours - break_h)
        
        # 基本給の計算
        base_pay = actual_hours * wage
        
        # 深夜手当の計算（深夜分は時給の0.25倍を追加で支給）
        night_pay = night_h * (wage * 0.25)
        
        # 合計
        total = base_pay + night_pay + trans
        
        # 結果を表示エリアに出現させる
        result_area = document.querySelector("#result-area")
        result_area.style.display = "block"
        
        # 各項目を書き換え
        document.querySelector("#res-base").innerText = f"{int(base_pay):,} 円"
        document.querySelector("#res-night").innerText = f"{int(night_pay):,} 円"
        document.querySelector("#res-trans").innerText = f"{int(trans):,} 円"
        document.querySelector("#res-total").innerText = f"{int(total):,} 円"
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
