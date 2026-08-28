import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

st.set_page_config(
    page_title="Codebasics Enterprise Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    [data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
        padding-top: 1.5rem;
    }
    .brand-box {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border: 1px solid #374151;
        padding: 24px 16px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
    }
    .stTextInput input {
        background-color: #111827 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #374151 !important;
        padding: 18px 20px !important;
        font-size: 16px;
    }
    .stTextInput input:focus {
        border: 2px solid #6366f1 !important;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.3);
    }
    .stButton button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border-radius: 12px;
        font-weight: 600;
        border: none;
        padding: 12px 20px;
        font-size: 15px;
        letter-spacing: 0.3px;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(99, 102, 241, 0.6);
        opacity: 0.95;
    }
    .response-container {
        background-color: #111827;
        border: 1px solid #374151;
        border-left: 5px solid #6366f1;
        padding: 24px;
        border-radius: 14px;
        margin-top: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    .metric-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        padding: 12px 16px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
        <div class="brand-box">
            <span style="font-size: 40px;">⚡</span>
            <h2 style="margin: 10px 0 5px 0; color: #ffffff; font-size: 22px; font-weight: 700;">Codebasics AI</h2>
            <p style="color: #9ca3af; font-size: 13px; margin: 0; font-weight: 500;">Enterprise Intelligence Hub</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🗂️ Knowledge Vault")
    if st.button("🔄 Sync Vector Database", use_container_width=True):
        with st.spinner("Indexing enterprise documents..."):
            try:
                create_vector_db()
                st.success("Database synchronized successfully!")
            except Exception as e:
                st.error(f"Sync failed: {e}")
                
    st.markdown("---")
    st.markdown("### 📊 System Telemetry")
    st.markdown("""
        <div class="metric-card">
            <p style="color: #9ca3af; font-size: 12px; margin: 0;">Active LLM Engine</p>
            <p style="color: #ffffff; font-size: 16px; font-weight: 600; margin: 2px 0 0 0;">Gemini Flash</p>
        </div>
        <div class="metric-card">
            <p style="color: #9ca3af; font-size: 12px; margin: 0;">Retrieval Framework</p>
            <p style="color: #ffffff; font-size: 16px; font-weight: 600; margin: 2px 0 0 0;">FAISS Vector Index</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.caption("🔒 Secured Corporate Environment")

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800; font-size: 42px; letter-spacing: -0.5px;'>Ask Your Corporate Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 18px; margin-bottom: 40px;'>Instant, verified answers mapped directly from enterprise records.</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    question = st.text_input("", placeholder="🔍 Type your query here... (e.g., What is the course validity?)")

if question:
    with col2:
        with st.spinner("Analyzing knowledge base..."):
            try:
                chain = get_qa_chain()
                response = chain.invoke(question)
                
                st.markdown(f"""
                    <div class="response-container">
                        <div style="display: flex; align-items: center; margin-bottom: 12px;">
                            <span style="font-size: 20px; margin-right: 8px;">🤖</span>
                            <h3 style="color: #ffffff; margin: 0; font-size: 18px; font-weight: 700;">Verified Assistant Output</h3>
                        </div>
                        <p style='color: #e5e7eb; font-size: 16px; line-height: 1.7; margin: 0;'>{response}</p>
                    </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.markdown(f"""
                    <div class="response-container" style="border-left-color: #ef4444;">
                        <h3 style="color: #ef4444; margin: 0 0 8px 0; font-size: 18px;">⚠️ Execution Exception</h3>
                        <p style='color: #fca5a5; font-size: 15px; margin: 0;'>{e}</p>
                    </div>
                """, unsafe_allow_html=True)