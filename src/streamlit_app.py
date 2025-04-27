# src/app/streamlit_app.py

import streamlit as st
from pipelines.rag_pipeline import load_rag_pipeline, ask_question


st.set_page_config(page_title="📈 Financial Reports Assistant", page_icon="📄")

# Title
st.title("📈 Financial Reports Assistant")

st.markdown("Ask any question about financial filings (10-K reports) from companies!")

# Load RAG pipeline once (cached)
@st.cache_resource
def load_chain():
    return load_rag_pipeline()

chain = load_chain()

# User input
query = st.text_input("Ask a question:")

if st.button("Ask") or query:
    if query.strip() == "":
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking... 🤔"):
            result = ask_question(chain, query)

        st.success("Here's the answer:")

        st.write(result["result"])

        st.divider()

        st.subheader("🔎 Source Documents:")
        for source_doc in result["source_documents"]:
            company = source_doc.metadata.get("company", "Unknown Company")
            date = source_doc.metadata.get("filing_date", "Unknown Date")
            section = source_doc.metadata.get("section", "Unknown Section")
            st.markdown(f"- **{company}** ({date}) [{section}]")

st.divider()

st.caption("Powered by RAG 🧠 + Ollama 🚀 + LangChain 🔗")
