import os
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

def get_legal_chain():
    """
    Returns a LangChain conversational chain using Google Gemini for legal summarization.
    """
    # Check for Gemini API key
    if "GOOGLE_API_KEY" not in os.environ:
        raise ValueError("Please set your GOOGLE_API_KEY environment variable.")

    # Initialize Gemini LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.3)

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a legal assistant AI. "
         "Summarize contract clauses in plain English. "
         "Highlight potential risks and provide actionable advice in a concise and readable way."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    memory = ConversationBufferMemory(memory_key="history", return_messages=True)
    chain = ConversationChain(llm=llm, memory=memory, prompt=prompt, verbose=False)
    return chain
