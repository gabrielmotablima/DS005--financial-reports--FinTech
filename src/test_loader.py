# src/loaders/test_loader.py

from loaders.loader import load_json_documents, split_documents
import config.config as config

docs = load_json_documents(config.EXTRACTED_DIR)  # adjust path if needed

print(f"Loaded {len(docs)} documents!")

chunks = split_documents(docs, chunk_size=500, chunk_overlap=50)

print(f"Generated {len(chunks)} chunks!")
print("Sample chunk content:")
print(chunks[0].page_content[:500])
print("Metadata:", chunks[0].metadata)