import streamlit as st
import google.generativeai as genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Customer Support AI Agent")
st.write("Ask me anything about our products or your recent orders!")

user_input = st.text_input("Your Message:")

if st.button("Send") and user_input:
    prompt = f"You are a helpful customer support agent. Keep answers brief. Customer: {user_input}\nAgent:"
    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception:
        st.write("I am experiencing technical difficulties. Please try again.")
