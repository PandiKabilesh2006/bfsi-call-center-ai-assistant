from src.pipeline import BFSIAssistantPipeline

assistant=BFSIAssistantPipeline("data/alpaca_dataset.json","data/knowledge_docs")

while True:
    query=input("\nEnter query (or type exit): ")

    if(query.lower()=="exit"):
        break

    result=assistant.handle_query(query)

    print("\nResponse Source:",result["source"])
    print("Response:",result["response"])
