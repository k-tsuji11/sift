from pyscript import document, window
from pyodide.ffi import create_proxy

def calculate(event):
    try:
        # 値の取得
        wage = float(document.querySelector("#wage").value)
        hours = float(document.querySelector("#hours").value)
        break_h = float(document.querySelector("#break_hours").value)
        night_h = float(document.querySelector("#night_hours").value)
        trans = float(document.querySelector("#transport").value)

        # ロジック
        actual_hours = max(0, hours - break_h)
        base_pay = actual_hours * wage
        night_pay = night_h * (wage * 0.25)
        total = base_pay + night_pay + trans

        # 表示の更新
        document.querySelector("#result-area").style.display = "block"
        document.querySelector("#res-base").innerText = f"{int(base_pay):,} 円"
        document.querySelector("#res-night").innerText = f"{int(night_pay):,} 円"
        document.querySelector("#res-trans").innerText = f"{int(trans):,} 円"
        document.querySelector("#res-total").innerText = f"{int(total):,} 円"
        
    except Exception as e:
        window.alert("数値を正しく入力してください")

# ボタンにクリックイベントを登録する
calc_button = document.querySelector("#calc-btn")
click_proxy = create_proxy(calculate)
calc_button.addEventListener("click", click_proxy)
