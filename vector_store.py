from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

def create_faiss_index(docs):
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )
    db = FAISS.from_documents(docs, embeddings)
    return db
