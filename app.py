import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Initialize Gemini Client
client = genai.Client()

st.title("AI Document Summarizer")
st.write("Summarize long text blocks using Google Gemini.")

text_input = st.text_area("Paste your text here:", height=200)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Generating summary..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=f"Summarize the following text concisely:\n\n{text_input}",
                )
                st.subheader("Summary:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text first.")
