import streamlit as st
import time

st.title("streamlit beginner!!!!")
st.write("Display Image")

option = st.selectbox(
    "あなたが好きな数字を教えて下さい",
    list(range(1,10))
)

"あなたの好きな数字は",option,"です"

st.write("Progress Bar")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done"

left_column, right_colum = st.beta_columns(2)

button = left_column.button("右カラムに文字を表示")
if button:
    right_colum.write("ここは右カラムです")

expander = st.expander("問い合わせ1")
expander.write("問い合わせ内容1の回答")
expander1 = st.expander("問い合わせ2")
expander1.write("問い合わせ内容2の回答")
expander2 = st.expander("問い合わせ3")
expander2.write("問い合わせ内容3の回答")
