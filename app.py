import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
import pypdf

# Load environment variables from .env
load_dotenv()

# Initialize Gemini Client
client = genai.Client()

st.title("AI Document Summarizer")
st.write("Summarize text or upload a PDF using Google Gemini.")

input_choice= st.radio("Choose how to input your document:", ["Paste your text here:", "Upload a PDF"])

text_input = " "

if input_choice == "Paste your text here:":
    text_input = st.text_area("Enter your text here:", height=200)
else:
    uploaded_file = st.file_uploader("Upload a PDF file:", type=["pdf"])
    if uploaded_file is not None:
        reader = pypdf.PdfReader(uploaded_file)
        for page in reader.pages:
            text_input += page.extract_text()
        st.success("PDF loaded successfully! Click Summarize below.")

if st.button("Summarise"):
    if text_input.strip():
        with st.spinner("Generating summary..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=f"Summarize the following text concisely:\n\n{text_input}",
                )
                st.subheader("Summary:")
                st.write(response.text)
                st.download_button(
                    label="Download Summary",
                    data=response.text,
                    file_name="summary.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text or upload a PDF first.")
