import streamlit as st
import requests

url = 'https://chat.openai.com/'
key = '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'

response = requests.get(url, headers={'Authorization': 'Bearer ' + key})

if response.status_code == 200:
    data = response.json()
    st.write(data)
else:
    st.error(response.text)
