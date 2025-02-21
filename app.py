from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

st.title("Langchain-DeepSeek-R1 app")

template = """
Question: {question}
Answer: Let us think about this step by step before giving an answer.
"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1:7b", device="cuda")

chain = prompt | model

question = st.chat_input("Enter your question here:")

if question:
    st.write(chain.invoke({"question": question}))
