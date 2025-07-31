import streamlit as st
from dotenv import load_dotenv
from load_pdf import load_and_split_pdf
from vector_store import create_faiss_index
from QAchain import get_qa_chain

load_dotenv()

st.set_page_config(layout="wide")
st.title("💼 AI Financial Statement Chatbot (LangChain + OpenRouter)")

uploaded_file = st.file_uploader("Upload your bank/finance statement (PDF)", type=["pdf"])
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    st.info("Processing document...")
    docs = load_and_split_pdf("temp.pdf")
    vectordb = create_faiss_index(docs)
    qa = get_qa_chain(vectordb)

    st.success("Chatbot ready! Ask any financial question.")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_query = st.text_input("Ask something about your statement:")
    if user_query:
        result = qa.run({"question": user_query, "chat_history": st.session_state.chat_history})
        st.session_state.chat_history.append((user_query, result))

    for i, (q, a) in enumerate(reversed(st.session_state.chat_history[-5:])):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
