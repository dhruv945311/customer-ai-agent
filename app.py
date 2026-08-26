import streamlit as st
import requests

# Your exact AQ token
api_key = "AQ.Ab8RN6K5_QlvAj16K5LXrRjgM0Tgk_j8Yxaw4dxXElocUOJQrg"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

st.title("Customer Support AI Agent")
st.write("Ask me anything about our products or your recent orders!")

user_input = st.text_input("Your Message:")

if st.button("Send") and user_input:
    prompt = f"You are a helpful customer support agent. Keep answers brief. Customer: {user_input}\nAgent:"
    
    # We build the exact payload Google expects natively
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    try:
        # Bypassing the SDK and sending directly to the API endpoint
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            answer = response.json()['candidates'][0]['content']['parts'][0]['text']
            st.write(answer)
        else:
            st.write(f"Direct API Error: {response.text}")
    except Exception as e:
        st.write(f"Connection Error: {e}")
