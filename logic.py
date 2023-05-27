import streamlit as st

st.title("수리논리학 계산기")

buttons = ["∧(and)", "∨(or)", "¬(not)", "→(imply)", "↔(equal)"]



if st.button("∧(and)", key="and"):
    st.text_input(label="", value=str("∧"), key="and_in", persist=True)

if st.button("∨(or)", key="or"):
    st.text_input(label="", value=str("∨"), key="or_in", persist=True)
    
if st.button("¬(not)", key="not"):
    st.text_input(label="", value=str("¬"), key="not_in", persist=True)

if st.button("→(imply)", key="imply"):
    st.text_input(label="", value=str("→"), key="imply_in", persist=True)

if st.button("↔(equal)", key="equal"):
    st.text_input(label="", value="↔", key="equal_in", persist=True)
    
for button in buttons:
    st.button(button, key=button)
