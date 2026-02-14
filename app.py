import streamlit as st
from src.pipeline import BFSIAssistantPipeline

st.set_page_config(
    page_title="BFSI AI Assistant",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 BFSI Call Center AI Assistant")
st.markdown("Lightweight, compliant AI system with dataset priority, SLM, and RAG.")

@st.cache_resource
def load_pipeline():
    return BFSIAssistantPipeline(
        "data/alpaca_dataset.json",
        "data/knowledge_docs"
    )

assistant=load_pipeline()

user_query=st.text_input("Enter your banking/financial query:")

if(st.button("Submit")):
    if(user_query.strip() == ""):
        st.warning("Please enter a query.")
    else:
        with st.spinner("Processing..."):
            result = assistant.handle_query(user_query)

        st.success("Response Generated")

        st.markdown("### 📌 Response")
        st.write(result["response"])

        st.markdown("---")
        st.caption(f"Response Source: {result['source']}")
