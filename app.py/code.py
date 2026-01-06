import streamlit as st

# アプリのタイトル
st.title("バイト給料計算アプリ")

# 入力フォーム
with st.form("my_form"):
    hourly_wage = st.number_input("時給を入力してください (円)", min_value=0, value=1200, step=10)
    working_hours = st.number_input("働いた時間を入力してください (時間)", min_value=0.0, value=5.0, step=0.5)
    
    # 計算ボタン
    submitted = st.form_submit_button("計算する")

# ボタンが押された時の処理
if submitted:
    total_salary = hourly_wage * working_hours
    st.divider()
    st.subheader(f"合計給料: {total_salary:,.0f} 円")
    st.balloons() # お祝いの風船を飛ばす演出