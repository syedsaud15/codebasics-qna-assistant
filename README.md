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
🚀 Getting Started Locally
Prerequisites
Python 3.10 or higher installed on your system.

A valid Google AI Studio API Key.

Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/syedsaud15/codebasics-qna-assistant.git](https://github.com/syedsaud15/codebasics-qna-assistant.git)
cd codebasics-qna-assistant
Create and activate a virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and add your Google API key:

Code snippet
GOOGLE_API_KEY=your_actual_api_key_here
Run the Application:

Bash
streamlit run app.py
💡 Usage Guide
Launch the application via the local Streamlit URL (http://localhost:8501).

Click on "🔄 Sync Vector Database" in the sidebar to process the CSV and generate local FAISS embeddings.

Type any corporate or course-related query into the central interface to receive instant, verified answers mapped directly from enterprise records.
