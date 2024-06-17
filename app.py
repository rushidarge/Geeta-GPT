import streamlit as st
import requests
import json
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI


import os
# Set the GOOGLE_API_KEY environment variable
os.environ["GOOGLE_API_KEY"] = "YOUR API KEY"

from langchain_google_genai import ChatGoogleGenerativeAI
# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# loading the embedding model
model_name = "BAAI/bge-small-en-v1.5"
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}
global hf
hf = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
)

# loading the vector database
global retriever
global new_db
new_db = FAISS.load_local("faiss_index", hf)
retriever = new_db.as_retriever(search_kwargs={"k":5})


def faiss_search(query):
  """
  Performs text similarity search using FAISS.

  Args:
      query: The user's query string.
      faiss_index: The loaded FAISS index for efficient retrieval.
      hf: The Hugging Face library for embedding generation.

  Returns:
      A list of top K similar document IDs based on the query.
  """
  context=retriever.get_relevant_documents(query)
  return context

def llm_query(context, question):
    '''
    Get the context and question from the user and return the answer

    Args:
        context: The context from the user
        question: The question asked by the user

    Returns:
        The answer from the model
    '''
    global llm
    prompt_template = f"""Final Prompt: Use the following pieces of information to answer the user's question.
    If you don't know the answer, just say that you don't know; strictly don't add anything from your side.

    Context: {context}
    Question: {question}

    Only return the helpful answer. Give a direct answer with reference to the context. Answer it like Krishna, in a melodious and little bit brief way. 
    Answer:
    """
    response = llm.invoke(prompt_template)
    return response.content
 
def chat(user_input):
  """
  Processes user input and retrieves relevant documents using FAISS.

  Args:
      user_input: The user's query string.
      documents: The processed and prepared documents.

  Returns:
      A response string based on the retrieved documents.
  """
  # response 
  retrieved_docs = faiss_search(user_input)
  context_page_content = [doc.page_content for doc in retrieved_docs]
  context_page_content_as_text = '\n'.join(context_page_content)

  # RAG logic 
  final_output = llm_query(context_page_content_as_text, user_input)
  return final_output

if "message_history" not in st.session_state:
  st.session_state["message_history"] = []

message_history = st.session_state["message_history"]

user_input = st.chat_input(placeholder="Ask question Krishna will answer your questions!!!")

if user_input:
  message_history.append({"role": "You", "content": user_input})
  response = chat(user_input)
  message_history.append({"role": "Krishna", "content": response})

st.subheader("Bhagwat Geeta 🦚")
for message in message_history:
  st.write(f"{message['role']}: {message['content']}")


# to run this streamlit application use following command
# streamlit run app.py
