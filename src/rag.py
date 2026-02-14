import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class RAGEngine:
    def __init__(self, docs_path):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.documents = []
        self.doc_texts = []
        for filename in os.listdir(docs_path):
            file_path = os.path.join(docs_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                self.documents.append({
                    "name": filename,
                    "content": text
                })
                self.doc_texts.append(text)
        self.embeddings = self.model.encode(self.doc_texts)

    def retrieve(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(
            query_embedding,
            self.embeddings
        )[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        retrieved_docs = [self.documents[i]["content"] for i in top_indices]
        return retrieved_docs
