import openai
import streamlit as st

openai.api_key = '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'

messages = []
content = ""
chat_response = ""

st.title("수리논리학 계산기")

n = int(st.text_input("개별적 사실을 몇 개 입력하시겠습니까? (최대 5개)")) or 0

if n > 0:
    infer = []
    for i in range(n):
        infer.append(st.text_input("개별적 사실"))
else:
    infer = []

if st.button("입력", key="button1"):
    for i in range(n):
        infer[i] = st.text_input("개별적 사실", value = "")
    Qinfer = st.text_input("소전제")
    
    if st.button("출력", key="button2"):
        for j in range(n):
            content = f"귀납법으로 추론, 개별적 사실은 {infer}, 소전제는 {Qinfer}, 결론만 출력"
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content}
            ]
        )

        # 응답 결과 표시
        chat_response = completion.choices[0].message.content
        st.text(chat_response)
