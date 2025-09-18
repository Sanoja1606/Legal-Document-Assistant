import streamlit as st
from langchain_legal import get_legal_chain
import PyPDF2
import os

st.set_page_config(page_title="AI Legal Assistant", page_icon="⚖️", layout="centered")
st.title("⚖️ AI Legal/Contract Assistant")
st.write("Upload a contract (PDF) or paste the text below. The AI will summarize clauses in plain English and highlight potential risks.")


if "GOOGLE_API_KEY" not in os.environ:
    st.warning("Please set your GOOGLE_API_KEY environment variable before using the app.")
else:
    chain = get_legal_chain()


    uploaded_file = st.file_uploader("Upload a PDF Contract", type=["pdf"])
    text_input = st.text_area("Or paste contract text here:")

    contract_text = ""

    if uploaded_file:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            contract_text += page.extract_text() + "\n"

    if text_input:
        contract_text += "\n" + text_input

    if st.button("Summarize & Analyze Contract"):
        if contract_text.strip():
            with st.spinner("Analyzing contract with Gemini..."):
                response = chain.run(input=contract_text)
            st.subheader("📄 Contract Summary & Advice")
            st.markdown(response)
        else:
            st.warning("Please upload a PDF or paste some text.")
