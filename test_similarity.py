from src.similarity import SimilaritySearch

search_engine=SimilaritySearch("data/alpaca_dataset.json")

query=input("Enter query: ")

response=search_engine.search(query)

if response:
    print("\nMatched Response:")
    print(response)
else:
    print("\nNo strong match found.")
