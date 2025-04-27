# src/embeddings/embedder.py

from langchain_huggingface import HuggingFaceEmbeddings

def load_embedder(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embedder = HuggingFaceEmbeddings(model_name=model_name)
    return embedder
