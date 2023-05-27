import streamlit as st

st.title("수리논리학 계산기")

if st.button("∧(and)", key="and"):
    st.text_input(label="∧(and)", value="∧", key="and_in", persist=True)

if st.button("∨(or)", key="or"):
    st.text_input(label="∨(or)", value="∨", key="or_in", persist=True)
    
if st.button("¬(not)", key="not"):
    st.text_input(label="¬(not)", value="¬", key="not_in", persist=True)

if st.button("→(imply)", key="imply"):
    st.text_input(label="→(imply)", value="→", key="imply_in", persist=True)

if st.button("↔(equal)", key="equal"):
    st.text_input(label="↔(equal)", value="↔", key="equal_in", persist=True)
