import streamlit as st
import requests

# OpenAI API 키를 생성합니다.
# https://openai.com/blog/api-keys/

# API URL과 키를 설정합니다.
url = 'https://api.openai.com/v1/engines/davinci/completions'
key = 'YOUR API KEY'

# 사용자 입력을 받습니다.
prompt = st.text_input('Enter a prompt:')

# API에 요청을 보냅니다.
response = requests.post(url, headers={'Authorization': 'Bearer ' + key}, json={'prompt': prompt, 'temperature': 0.7, 'max_tokens': 100})

# 응답을 처리합니다.
if response.status_code == 200:
    # 응답이 성공적이면 데이터를 처리합니다.
    data = response.json()
    st.write(data['choices'][0]['text'])
else:
    # 응답이 실패하면 오류 메시지를 표시합니다.
    st.error(response.text)
