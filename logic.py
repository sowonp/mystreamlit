import openai
import streamlit as st

openai.api_key = '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'

messages = []
content = ""
chat_response = ""

st.title("수리논리학 계산기")

n = 0
if st.button("입력", key="number1"):
    n = st.text_input("개별적 사실을 몇 개 입력하시겠습니까? (최대 5개)", key="infer")
if n == "" or n == "0":
    n = 0
else:
    n = int(n.split()[0])

if n > 0:
    infer = []
    if st.button("입력", key="button1"):
        for i in range(n):
            infer[i] = st.text_input(f"개별적 사실", {infer[i]}, value = "", key=f"infer{i}")
        Qinfer = st.text_input("소전제", value = "", key="Qinfer")
        
        if st.button("입력", key="button2"):
            for i in range(n):
                content = f"귀납법으로 추론, 개별적 사실은 {infer[i]}, 소전제는 {Qinfer}, 결론만 출력"
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": content}
                ]
            )

            chat_response = completion.choices[0].message.content
            st.text(chat_response)
else:
    infer = []
