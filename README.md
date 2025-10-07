# 💼 FinGPT – Conversational Financial Statement Assistant

Welcome to **FinGPT**, your AI-powered assistant for understanding and querying your financial or bank statements!  
Built with **Streamlit**, **LangChain**, **OpenRouter**, and **FAISS** for blazing-fast, intelligent document Q&A.

---

## 🚀 Features

- **📄 Upload PDF Statements:** Instantly process your bank or finance PDFs.
- **💬 Conversational Q&A:** Ask questions in natural language and get clear, concise answers.
- **🔍 Semantic Search:** Finds relevant information using advanced vector search (FAISS).
- **🔒 Secure:** API keys managed via `.env` for your privacy.
- **⚡ Fast & Easy:** No setup hassle—just upload and chat!

---
## 🗂️ Project Structure

- `app.py` — Main Streamlit app
- `load_pdf.py` — PDF loader & splitter
- `vector_store.py` — FAISS vector index creator
- `QAchain.py` — Conversational retrieval chain setup
- `requirement.txt` — Python dependencies

---

## 🛠️ Getting Started

### 1. Prerequisites

- Python 3.8+
- [OpenRouter API key](https://openrouter.ai/)

### 2. Installation

```sh
git clone <your-repo-url>
cd <your-repo-directory>
pip install -r requirement.txt
```

### 3. Configuration

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
```

### 4. Run the App

```sh
streamlit run app.py
```

---

## ✨ Example

1. **Upload** your PDF statement.
2. **Ask:**  
   - "What was my total spending last month?"  
   - "List all transactions over $500."  
   - "What is my current balance?"

3. **Get instant answers!**

---
