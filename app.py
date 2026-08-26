import streamlit as st
import google.generativeai as genai
import os

# Clear any stuck secrets
if "GEMINI_API_KEY" in os.environ:
    del os.environ["GEMINI_API_KEY"]

# Your AQ format token
api_key = "AQ.Ab8RN6K5_QlvAj16K5LXrRjgM0Tgk_j8Yxaw4dxXElocUOJQrg"
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
    except Exception as e:
        st.write(f"Google API Error: {e}")
