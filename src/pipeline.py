
from src.guardrails import run_guardrails
from src.similarity import SimilaritySearch
from src.slm import LocalSLM
from src.rag import RAGEngine

class BFSIAssistantPipeline:
  
    def __init__(self,dataset_path,docs_path):
        self.similarity_engine=SimilaritySearch(dataset_path)
        self.slm=LocalSLM()
        self.rag=RAGEngine(docs_path)

    def handle_query(self, query):
        blocked,message=run_guardrails(query)
        if(blocked):
            return{
                "source":"Guardrails",
                "response":message
            }
        similarity_response=self.similarity_engine.search(query)
        if(similarity_response):
            return{
                "source":"Dataset",
                "response":similarity_response
            }
        rag_keywords = [
            "policy",
            "penalty",
            "interest",
            "approval",
            "credit score",
            "tenure",
            "charges",
            "foreclosure"
        ]

        if(any(keyword in query.lower() for keyword in rag_keywords)):
            retrieved_docs=self.rag.retrieve(query)
            if(retrieved_docs):
                context=retrieved_docs[0]
                rag_prompt=(
                    "You are a BFSI assistant. " 
                    "Answer strictly using the provided policy context.\n\n"
                    f"Policy Context:\n{context}\n\n"
                    f"User Query: {query}\nAssistant:"
                )
                response=self.slm.generate_response(rag_prompt)
                return{
                    "source":"RAG",
                    "response":response
                }
        slm_response=self.slm.generate_response(query)
        return{
            "source":"SLM",
            "response":slm_response
        }
