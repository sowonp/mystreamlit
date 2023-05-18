import streamlit as st
import bard

# Bard API 키를 생성합니다.
# https://bard.ai/docs/keys

# Streamlit 앱에서 Bard API 키를 설정합니다.
st.set_credentials("https://bard.google.com/", "b41f691c-ee31-4c6c-a2d1-d320b6be293d")

# Bard API를 호출합니다.
prompt = "Write a story about a dragon"
response = bard.generate(prompt, max_tokens=100)

# Bard API의 응답을 Streamlit 앱에 표시합니다.
st.write(response)
