**Legal AI Assistant** ⚖️
This project is a user-friendly AI Legal Assistant built with Python, LangChain, and Google Gemini. It's designed to help you quickly understand complex legal documents, such as contracts. The application uses the advanced capabilities of the Gemini large language model to summarize contract clauses in plain English, highlight potential risks, and provide actionable advice.

*Features* ✨
PDF Processing: Upload a PDF contract directly to the app for text extraction and analysis.

Text Input: Paste contract text into a text area for analysis.

AI-Powered Summaries: The gemini-1.5-flash-latest model distills complex legal jargon into simple, clear summaries.

Risk Highlighting: The AI identifies clauses that could be problematic (e.g., related to liability or termination).

Actionable Advice: Alongside potential risks, the tool offers practical advice to help you navigate legal documents.

*How It Works* 🧠
The application uses a LangChain conversational chain. A Streamlit front end provides the user interface. When you input text or upload a PDF, the application sends the content to the Gemini model via the LangChain chain. The model, instructed to act as a legal assistant, then generates a summarized and analyzed response, which is displayed in the app.

*Prerequisites*🛠️
Python 3.8+

A Google Cloud Project with the Generative Language API enabled to get your API key.

*Sample Upload*
<img width="1747" height="894" alt="legal_assistant" src="https://github.com/user-attachments/assets/309e50a8-ffff-4c5a-93f4-c49e44ad39ad" />


*Getting Started* 🚀
Clone the repository (or save the provided code files) to your local machine.

Install the required libraries:
pip install streamlit langchain langchain-google-genai pypdf2

Set your Google API Key: The application uses an environment variable to securely access your key.

macOS/Linux:
export GOOGLE_API_KEY="your-api-key-here"

Windows:
set GOOGLE_API_KEY="your-api-key-here"
Remember to replace "your-api-key-here" with your actual key.

Run the application:
streamlit run app.py
The application will open in your web browser, and you're ready to start analyzing documents!

