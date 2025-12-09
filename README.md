# 🧠💸 FinGPT — Conversational Financial Statement Assistant

Welcome to **FinGPT**, your AI-powered assistant for understanding and querying financial or bank statements.  
Built with Streamlit, LangChain, OpenRouter, and FAISS for blazing-fast, intelligent document Q&A. 🚀

Features ✨
- 📄 Upload PDF Statements: Instantly process your bank or financial PDFs.
- 💬 Conversational Q&A: Ask questions in natural language and get clear, concise answers.
- 🔍 Semantic Search: Finds relevant information using advanced vector search (FAISS).
- 🔒 Secure: Keep API keys in a local .env for privacy.
- ⚡ Fast & Easy: No heavy setup — upload and chat!

Project Structure 📂
- app.py — Main Streamlit app 🖥️
- load_pdf.py — PDF loader & splitter 📑
- vector_store.py — FAISS vector index creator 🧾
- QAchain.py — Conversational retrieval/check logic 🤖
- requirement.txt — Python dependencies 🐍
- .env — Environment variables (API keys) 🔑

Getting Started 🚦

1. Prerequisites ✅
- Python 3.8+
- OpenRouter API key (or other model provider key) 🔑

2. Installation 🛠️

Clone the repository, change into the project directory, and install dependencies:

```bash
git clone https://github.com/SaniyaManiyar0102/FinGPT---Conversational-Financial-Assistant.git
cd FinGPT---Conversational-Financial-Assistant
pip install -r requirement.txt
```

3. Configuration ⚙️

Create a `.env` file in the project root (if it doesn't already exist) and add your API keys. Example:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://api.openai.com/v1
```

(Adjust variable names/values to match the provider you're using.) 📝

4. Run the App ▶️

Start the Streamlit app:

```bash
streamlit run app.py
```

Example Usage 🧩
1. Upload your PDF statement. 📤  
2. Ask questions like:
   - "What was my total spending last month?" 💸
   - "List all transactions over $500." 🧾
   - "What is my current balance?" 📊  
3. Get instant answers! ⚡
---
Happy building! 💬🔧
