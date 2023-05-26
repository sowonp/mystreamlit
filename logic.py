import streamlit as st

st.title("수리논리학 계산기")

if st.button("∧(and)", key="and"):
    st.text_input(value="∧", key="and_in")

if st.button("∨(or)", key="or"):
    st.text_input(value="∨", key="or_in")
    
if st.button("¬(not)", key="not"):
    st.text_input(value="¬", key="not_in")

if st.button("→(imply)", key="imply"):
    st.text_input(value="→", key="imply_in")

if st.button("↔(equal)", key="equal"):
    st.text_input(value="↔", key="equal_in")

