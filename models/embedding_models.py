from sentence_transformers import SentenceTransformer # pyright: ignore[reportMissingImports]
import numpy as np # pyright: ignore[reportMissingImports]


class EmbeddingModel:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Loads a local sentence-transformer model.
        """
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        """
        Converts list of texts into embeddings.
        """
        embeddings = self.model.encode(
            texts,
            show_progress_bar=False,
            convert_to_numpy=True
        )
        return np.array(embeddings).astype("float32")
