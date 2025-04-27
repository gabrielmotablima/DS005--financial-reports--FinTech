# src/config/config.py

from pathlib import Path


# Base Directories
DATA_DIR = Path("data/sample_10K")
EXTRACTED_DIR = str(DATA_DIR / "extracted")
RAW_DIR = str(DATA_DIR / "raw")

VECTOR_DB_DIR = str(Path("vectorstore"))

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # or your model

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
