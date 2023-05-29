#Scripts\activate.bat
#streamlit run app2.py

import openai
import streamlit as st

messages = []
content1 = ""
content2 = ""
chat_response = ""
infer = [0, 0, 0, 0, 0]

openai.api_key = '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'

st.title("수리논리학 계산기")
number_string = st.number_input("개별적 사실을 몇 개 입력받겠습니까? (최대 5개)", 1, 5)

number = int(number_string)
st.markdown("논리식 사용 시, 해당 기호들을 복사하여 사용하세요.")
st.markdown("¬   ∧    ∨    →")

for i in range(number):
    infer[i] = st.text_input(f"개별적 사실 {i+1}", key = f"infer{i}")
    
Ginfer2 = st.text_input("질문", key = "infer5")

st.text("<예시>")
st.text("개별적 사실 1: 홈플러스 = (5000 → 라면) ∧ (3000 → 커피)")
st.text("개별적 사실 2: 레스토랑 = (홈플러스 → (5000 → 라면)) ∧ (홈플러스 → (3000 → 커피)) ∧ ((라면 ∧ 커피) → 라면 세트)")
st.text("질문: 손님 = 레스토랑 → (5000 → 라면 세트)")
if st.button("입력", key = "button"):
    for i in range(number):
        content1 += f'"{infer[i]}", '
    content1 += f'앞의 문장들은 모두 참이다.'
    content2 = f'"{Ginfer2}"라는 문장을 참 또는 거짓으로 판단해라.'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "넌 논리식 계산기야."},
            {"role": "user", "content": content1},
            {"role": "user", "content": content2}
        ]
    )

# 응답 결과 표시
    chat_response = completion.choices[0].message.content
    st.text(chat_response)
