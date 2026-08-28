import os
import csv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Embeddings ke liye HuggingFace use ho raha hai
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})
vector_db_file_path = "faiss_index"

def create_vector_db():
    file_path = os.path.join(os.path.dirname(__file__), 'codebasics_faqs.csv')
    docs = []
    
    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            # Agar row mein 2 ya usse zyada items hain
            if len(row) >= 2:
                content = f"Question: {row[0]}\nAnswer: {row[1]}"
            else:
                # Agar CSV sirf ek column ki hai ya format alag hai
                content = row[0]
            docs.append(Document(page_content=content))
            
    # Agar pehli row header hai toh use hata sakte hain, par agar data kam hai toh rehne dein
    if len(docs) > 1:
        docs = docs[1:]
        
    if not docs:
        raise ValueError("CSV file khali hai!")
        
    vectordb = FAISS.from_documents(documents=docs, embedding=embeddings)
    vectordb.save_local(vector_db_file_path)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_qa_chain():
    if not os.path.exists(vector_db_file_path):
        raise FileNotFoundError("Pehle 'Create Knowledge Base' button par click karke database banao!")
        
    vectordb = FAISS.load_local(vector_db_file_path, embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    
    # Google Gemini initialization
    # Yeh line change karni hai:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the context, each question-answer pair is provided. If the answer is not found in the context, kindly state "I don't know." Do not try to make up things.

    CONTEXT:
    {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate.from_template(prompt_template)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | PROMPT
        | llm
        | StrOutputParser()
    )

    return chain