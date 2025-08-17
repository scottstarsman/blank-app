import streamlit as st
import requests
import os

api_key = os.environ.get("OPEN_AI_API_KEY_VAR")

st.title("🎈 OpenAI Completions Demo")
if api_key == None or api_key == "":
    api_key= st.text_area("API key:")
st.write(api_key)
# Text box for user content
user_input = st.text_area("Enter your prompt:")

# Button to send request
if st.button("Enter"):
    if not user_input:
        st.error("Please enter some text.")
    else:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-4",
            "messages": [
                {"role": "user", "content": user_input}
            ],
            "max_tokens": 150
        }
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data
            )
            if response.status_code == 200:
                result = response.json()
                st.markdown("**Result:**")
                st.write(result["choices"][0]["message"]["content"].strip())
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
