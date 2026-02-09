import numpy as np  # pyright: ignore[reportMissingImports]
from utils.db import load_faiss_index, load_metadata
from utils.embeddings import get_embeddings
from models.llm_ollama import OllamaLLM


class QueryEngine:
    def __init__(self):
        self.index = load_faiss_index()
        self.docs = load_metadata()

        # -------- CURRENT MODE (FAST + LOW RAM) --------
        self.llm = OllamaLLM("tinyllama")

        # -------- DRDO MODE (UNCOMMENT FOR BETTER ANSWERS) --------
        # self.llm = OllamaLLM("phi3:mini")
        # self.llm = OllamaLLM("mistral")

    def query(self, question, top_k=3):
        # -------- DRDO MODE (UNCOMMENT FOR DEEP SEARCH) --------
        # top_k = 6

        q_emb = get_embeddings([question])
        distances, indices = self.index.search(q_emb, top_k)

        results = []
        for i in indices[0]:
            results.append(self.docs[i])

        context = "\n\n".join(results)

        prompt = f"""
You are a DRDO offline AI assistant.

Answer in ONE SHORT LINE using only relevant information.
Do NOT repeat full document.
Be precise and technical.

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.llm.generate(prompt)
        return response
