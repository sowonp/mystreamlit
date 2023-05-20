import streamlit as st
import openai

openai.api_key = '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'

st.title("ChatGPT with Streamlit")

# 사용자 입력 받기
user_input = st.text_input("사용자 입력")

if user_input:
    # ChatGPT에 입력 전달 및 응답 받기
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    # 응답 결과 표시
    chat_response = completion.choices[0].message.content
    st.text("ChatGPT 응답")
    st.text(chat_response)
