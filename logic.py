import streamlit as st

deduction = {'bp':'0', 'spd':'0', 'resultd':'0'}
induction = {'indt':'0', 'spi':'0', 'resulti':'0'}
true = True

tab1, tab2= st.tabs(['연역법' , '귀납법']) # 탭 이름 1: 연역법, 2: 귀납법

with tab1: #tab 1 표시될 내용
    st.write("연역법")
    st.write("대전제 입력: ")
    bp = st.text_input("대전제 입력: ")
    deduction['bp'] = bp
    spd = st.text_input("소전제 입력: ")
    deduction['sp'] = spd
    st.write("결론: ", deduction['resultd'])
    
with tab2: #tab 2 표시될 내용
    st.write("귀납법")
    indf = st.text_input("개별적 사실 입력: ")
    induction['indf'] = indf
    spi = st.text_input("소전제 입력: ")
    induction['spi'] = spi
    st.write("결론: ", induction['resulti'])
