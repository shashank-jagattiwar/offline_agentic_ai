from sentence_transformers import SentenceTransformer  # pyright: ignore[reportMissingImports]
import numpy as np  # pyright: ignore[reportMissingImports]

# Load once (singleton-style)
_model = None

def load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def get_embeddings(texts: list[str]) -> np.ndarray:
    model = load_model()
    return model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )
