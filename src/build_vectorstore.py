# src/vectorstores/build_vectorstore.py

import argparse
from loaders.loader import load_json_documents, split_documents
from embeddings.embedder import load_embedder
from vectorstores.vector_store import save_vector_store
import config.config as config
from langchain_community.vectorstores import FAISS
from tqdm import tqdm

# Argument parser
parser = argparse.ArgumentParser(description="Build FAISS vectorstore for financial reports")
parser.add_argument("--limit", type=int, default=None, help="Number of documents to process (default: all)")
args = parser.parse_args()

# Load documents
docs = load_json_documents(config.EXTRACTED_DIR)  # adjust path if needed
print(f"Loaded {len(docs)} documents.")

# Apply limit if specified
if args.limit is not None:
    docs = docs[:args.limit]
    print(f"Processing only {len(docs)} documents (limit set).")
else:
    print(f"Processing all {len(docs)} documents.")

# Split documents
chunks = split_documents(docs, chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
print(f"Generated {len(chunks)} chunks.")

# Load embedder
embedder = load_embedder(model_name=config.EMBEDDING_MODEL)

# Embed + Create Vector Store
print("Embedding and building FAISS index...")
db = FAISS.from_documents(
    documents=tqdm(chunks, desc="Embedding chunks"),
    embedding=embedder
)

# Save vectorstore
save_vector_store(db, config.VECTOR_DB_DIR)
print(f"Vector store saved at {config.VECTOR_DB_DIR}")
