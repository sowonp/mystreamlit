import streamlit as st
import requests

# API URL과 키를 설정합니다.
url = 'https://chat.openai.com/'
key = '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'

# API에 요청을 보냅니다.
response = requests.get(url, headers={'Authorization': 'Bearer ' + key})

# 응답을 처리합니다.
if response.status_code == 200:
    # 응답이 성공적이면 데이터를 처리합니다.
    data = response.json()
    st.write(data)
else:
    # 응답이 실패하면 오류 메시지를 표시합니다.
    st.error(response.text)
