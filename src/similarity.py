import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SimilaritySearch:
    def __init__(self,dataset_path,threshold=0.75):
        self.model=SentenceTransformer("all-MiniLM-L6-v2")
        self.threshold=threshold

        with open(dataset_path,"r") as f:
            self.data=json.load(f)

        self.instructions=[
            item["instruction"]+" "+item["input"]
            for item in self.data
        ]

        self.embeddings=self.model.encode(self.instructions)

    def search(self,query):
        query_embedding=self.model.encode([query])
        similarities=cosine_similarity(query_embedding,self.embeddings)[0]

        best_idx=np.argmax(similarities)
        best_score=similarities[best_idx]

        if best_score>=self.threshold:
            return self.data[best_idx]["output"]

        return None
