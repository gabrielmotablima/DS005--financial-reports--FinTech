# src/pipelines/rag_pipeline.py

from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from vectorstores.vector_store import load_vector_store
from embeddings.embedder import load_embedder
import config.config as config

def load_rag_pipeline():
    # Load embedder
    embedder = load_embedder(model_name=config.EMBEDDING_MODEL)

    # Load vectorstore
    db = load_vector_store(embeddings=embedder, path=config.VECTOR_DB_DIR)

    # Load Ollama model
    llm = ChatOllama(
        model="qwen2.5:0.5b",
        temperature=0.2
    )

    # Build RetrievalQA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(search_kwargs={"k": 5}),
        return_source_documents=True
    )

    return qa_chain

def ask_question(chain, query):
    result = chain.invoke(query)
    return result
