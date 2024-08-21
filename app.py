import streamlit as st

import google.generativeai as genai

st.title("My own AIChat")
genai.configure(api_key="AIzaSyCJyh1wQr51V8z5sqAYaEUwvoOihumawA8")
text = st.text_input("Give your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Search"):
 response = chat.send_message(text)
 response.text