# ⚡ Codebasics Enterprise Intelligence Assistant

An industry-grade RAG (Retrieval-Augmented Generation) web application built to extract precise answers from corporate records and FAQs using Google Gemini and LangChain, wrapped inside a high-performance Streamlit dashboard.

---

## 🛠️ Tech Stack & Architecture

* **Frontend & UI:** Streamlit (Custom Dark Theme, Telemetry Sidebars, Responsive Layouts)
* **Orchestration Framework:** LangChain (`RetrievalQA`, Prompt Templates)
* **LLM Engine:** Google Gemini (`gemini-1.5-flash`)
* **Vector Embeddings & Storage:** FAISS (Facebook AI Similarity Search) & HuggingFace Embeddings (`sentence-transformers`)
* **Data Processing:** Pandas (CSV Knowledge Source Management)

---

## 📂 Project Structure

```text
codebasics-qna-assistant/
│
├── app.py                  # Main Streamlit UI dashboard and entry point
├── langchain_helper.py     # RAG pipeline, LLM configuration, and vector DB logic
├── codebasics_faqs.csv     # Enterprise dataset containing institutional FAQs
├── requirements.txt        # Pinned dependency manifest
└── .gitignore              # Excludes virtual environments and local indices
