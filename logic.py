import streamlit as st

st.title("수리논리학 계산기")

buttons = ["∧(and)", "∨(or)", "¬(not)", "→(imply)", "↔(equal)"]

for button in buttons:
    st.button(button, key=button)
