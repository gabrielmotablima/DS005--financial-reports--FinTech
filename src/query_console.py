# src/pipelines/query_console.py

from pipelines.rag_pipeline import load_rag_pipeline, ask_question

def main():
    chain = load_rag_pipeline()

    print("\n🔎 Financial Reports Assistant 🔎")
    print("Type your question or 'exit' to quit.")
    while True:
        query = input("\nQuestion: ")
        if query.lower() in ["exit", "quit"]:
            break
        
        response = ask_question(chain, query)
        print("\nAnswer:\n", response["result"])

        # Show sources (optional)
        print("\nSource Documents:")
        for source_doc in response["source_documents"]:
            print(f"- {source_doc.metadata.get('company', 'Unknown Company')} ({source_doc.metadata.get('filing_date', 'Unknown Date')}) [{source_doc.metadata.get('section', 'Unknown Section')}]")

if __name__ == "__main__":
    main()
