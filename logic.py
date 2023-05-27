#Scripts\activate.bat
#streamlit run app2.py

#레스토랑 = (홈플러스 → (5000 → 라면)) ∧ (홈플러스 → (3000 → 커피)) ∧ ((라면 ∧ 커피) → 라면 세트)

import openai
import streamlit as st

messages = []
content = ""
chat_response = ""
infer = [0, 0, 0, 0, 0]

openai.api_key = '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'

st.title("수리논리학 계산기")
number_string = st.number_input("개별적 사실을 몇 개 입력받겠습니까? (최대 5개)", 1, 5)

number = int(number_string)

st.text("논리식 사용 시, 해당 기호들을 복사하여 사용하세요.")
st.text("¬ ∧ ∨ →")

for i in range(number):
    infer[i] = st.text_input(f"개별적 사실{i+1}", value = "홈플러스 = (5000 → 라면) ∧ (3000 → 커피)", key = f"infer{i}")
    
Ginfer2 = st.text_input("질문", value = "손님 = 레스토랑 → (5000 → 라면 세트)", key = "infer5")
if st.button("입력", key = "button"):
    for i in range(number):
        content += f'"{infer[i]}", '
    content += f'일 때, "{Ginfer2}"라는 문장은 성립하는가?'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #temperaturn = 9,
        messages=[
            {"role": "system", "content": "넌 똑똑한 소비자야."},
            {"role": "user", "content": content}
        ]
    )

# 응답 결과 표시
    chat_response = completion.choices[0].message.content
    st.text(chat_response)
