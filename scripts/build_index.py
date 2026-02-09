import faiss # pyright: ignore[reportMissingImports]
from utils.loader import load_documents
from utils.embeddings import get_embeddings
from utils.db import save_faiss_index, save_metadata

def build_index():
    docs = load_documents()

    if not docs:
        raise RuntimeError("No documents found in data/pdfs or data/docs")

    embeddings = get_embeddings(docs)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    save_faiss_index(index)
    save_metadata(docs)

    print(f"✅ FAISS index built successfully with {len(docs)} documents")

if __name__ == "__main__":
    build_index()
