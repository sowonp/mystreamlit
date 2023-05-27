import streamlit as st
from streamlit import button, column

st.title("수리논리학 계산기")

button1 = button("Button 1")
button2 = button("Button 2")

column(button1, button2)
