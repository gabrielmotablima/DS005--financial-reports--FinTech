# src/loaders/loader.py

import os
import json
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_json_documents(folder_path):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Directly access data (no "root" key anymore)
                metadata = {
                    "company": data.get("company", ""),
                    "filing_date": data.get("filing_date", ""),
                    "filing_type": data.get("filing_type", ""),
                    "state_location": data.get("state_location", ""),
                    "period_of_report": data.get("period_of_report", "")
                }

                # Extract interesting sections
                for section_key in ["item_1", "item_1A", "item_7", "item_8"]:
                    section_text = data.get(section_key, None)
                    if section_text:
                        doc = Document(
                            page_content=section_text,
                            metadata={**metadata, "section": section_key}
                        )
                        documents.append(doc)

    return documents


def split_documents(documents, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "],  # Try to split nicely at paragraphs, sentences, then words
    )
    return text_splitter.split_documents(documents)