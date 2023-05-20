import openai
import streamlit as st

openai.api_key = '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'

messages = []
content = ""
chat_response = ""

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        st.sidebar.title("추론하는 프로그램")
        st.sidebar.subheader("어떤법으로 추론하시겠습니까?")
               
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title'])
    
        app['function']()
def g():
    st.title("귀납법 프로그램 실행합니다.")
    Ginfer1 = st.text_input("개별적 사실", value="여러문장 입력시 ,로 구분해서 쓰시오")
    Ginfer2 = st.text_input("소전체")
    if st.button("입력"):
        content = f"귀납법으로 추론, 개별적 사실은 {Ginfer1}, 소전제는 {Ginfer2}, 결론만 출력"
        return content

def y():
    st.title("연역법 프로그램 실행합니다.")
    Yinfer1 = st.text_input("대전체")
    Yinfer2 = st.text_input("소전체")
    if st.button("입력"):
        content = f"연역법으로 추론, 대전제는 {Yinfer1}, 소전제는 {Yinfer2}, 결론만 출력"
        return content

infer = MultiApp()
infer.add_app("귀납법 입력", g)
infer.add_app("연역법 입력", y)
infer.run()

if content:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}]
    )
    chat_response = completion.choices[0].message.content
    st.write(chat_response)
    messages = [{"role": "assistant", "content": chat_response}]
