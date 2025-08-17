import streamlit as st
import requests
import os

api_key = os.environ.get("OPEN_AI_API_KEY_VAR")

st.title("🎈 OpenAI Chat Demo")
if api_key == None or api_key == "":
    api_key= st.text_area("API key:")
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

import pandas as pd
import streamlit as st

# Create a DataFrame with specified columns and 5 rows
data = {
    'Goal': [
        'Increase Sales',
        'Improve Customer Satisfaction',
        'Reduce Costs',
        'Expand Market Reach',
        'Enhance Product Quality'
    ],
    'Assessment': [
        'Quarterly Review',
        'Survey Results',
        'Expense Analysis',
        'Market Analysis',
        'Quality Audit'
    ],
    'Assessment Description': [
        'Review sales numbers and growth.',
        'Analyze customer feedback and ratings.',
        'Evaluate cost-saving measures.',
        'Assess new market opportunities.',
        'Inspect product quality improvements.'
    ]
}
df = pd.DataFrame(data)

# Display the DataFrame as a table in Streamlit
st.title('Goals and Assessments')
st.table(df)
