import faiss # pyright: ignore[reportMissingImports]
import numpy as np # pyright: ignore[reportMissingImports]
from sentence_transformers import SentenceTransformer # pyright: ignore[reportMissingImports]
from utils.db import load_faiss_index, load_metadata

class Retriever:
    def __init__(self):
        self.index = load_faiss_index()
        self.metadata = load_metadata()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def retrieve(self, query: str, top_k: int = 3):
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx in self.metadata:
                results.append(self.metadata[idx])

        return results
