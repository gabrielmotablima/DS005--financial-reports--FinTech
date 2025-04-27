# src/vectorstores/vector_store.py

from langchain_community.vectorstores import FAISS

def create_vector_store(embeddings, documents):
    db = FAISS.from_documents(documents, embeddings)
    return db

def save_vector_store(db, path):
    db.save_local(path)

def load_vector_store(embeddings, path):
    db = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    return db
