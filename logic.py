import streamlit as st

ded = {"bp":"대전제", "spd":"연역법 소전제", "rd":"연역법 결과"}
ind = {"indf":"개별적 사실", "spi":"귀납법 소전제", "ri":"귀납법 결과"}

tab1, tab2= st.tabs(['연역법' , '귀납법'])

with tab1:
    st.write("연역법")
    bp = st.text_input("대전제 입력: ", ded["bp"])
    spd = st.text_input("소전제 입력: ", ded["spd"])
    st.write("결론: ", ded["rd"])
    
with tab2:
    st.write("귀납법")
    indf = st.text_input("개별적 사실 입력: ", ind["indf"])
    spi = st.text_input("소전제 입력: ", ind["spi"])
    st.write("결론: ", ind["ri"])
