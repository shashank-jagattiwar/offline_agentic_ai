import faiss # pyright: ignore[reportMissingImports]
import pickle
from utils.config import FAISS_INDEX_PATH, METADATA_PATH

def save_faiss_index(index):
    faiss.write_index(index, FAISS_INDEX_PATH)

def load_faiss_index():
    return faiss.read_index(FAISS_INDEX_PATH)

def save_metadata(metadata):
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)

def load_metadata():
    with open(METADATA_PATH, "rb") as f:
        return pickle.load(f)
