import streamlit as st
import bard

url = 'https://bard.google.com/'
key = 'sb41f691c-ee31-4c6c-a2d1-d320b6be293d'

deduction = {'대전제':'0', '소전제':'0', '결론':'0'}
induction = {'개별적 사실':'0', '소전제':'0', '결론':'0'}
true = True

tab1, tab2= st.tabs(['연역법' , '귀납법']) # 탭 이름 1: 연역법, 2: 귀납법

with tab1: #tab 1 표시될 내용
    st.write("연역법")
    st.write("대전제 입력: ")
    bp = st.text_input("대전제 입력: ")
    deduction['대전제'] = bp
    sp = st.text_input("소전제 입력: ")
    deduction['소전제'] = sp
    st.write("결론: ", deduction['결론'])
    
with tab2: #tab 2 표시될 내용
    st.write("귀납법")
    indf = st.text_input("개별적 사실 입력: ")
    induction['개별적 사실'] = indf
    sp = st.text_input("소전제 입력: ")
    induction['소전제'] = sp
    st.write("결론: ", induction['결론'])
