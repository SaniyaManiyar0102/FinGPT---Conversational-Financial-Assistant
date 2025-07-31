from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
import os

def get_qa_chain(vectorstore):
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE"),
        model_name="gpt-3.5-turbo",
        temperature=0
    )
    qa = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=False,
        verbose=True
    )
    return qa
