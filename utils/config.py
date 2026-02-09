import os

# Base directory of the project
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# -------------------- DATA DIRECTORIES --------------------
DATA_DIR = os.path.join(BASE_DIR, "data")

PDF_DIR = os.path.join(DATA_DIR, "pdfs")
DOC_DIR = os.path.join(DATA_DIR, "docs")

# -------- DRDO MODE (UNCOMMENT WHEN USING LABVIEW FILES) --------
# LABVIEW_DIR = os.path.join(DATA_DIR, "labview")

# -------------------- VECTOR STORE --------------------
VECTOR_STORE_DIR = os.path.join(BASE_DIR, "vector_store")
FAISS_INDEX_DIR = os.path.join(VECTOR_STORE_DIR, "faiss_index")

FAISS_INDEX_PATH = os.path.join(FAISS_INDEX_DIR, "index.faiss")
METADATA_PATH = os.path.join(VECTOR_STORE_DIR, "metadata.pkl")

# -------------------- CREATE DIRS IF NOT EXIST --------------------
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(DOC_DIR, exist_ok=True)

# -------- DRDO MODE --------
# os.makedirs(LABVIEW_DIR, exist_ok=True)

os.makedirs(FAISS_INDEX_DIR, exist_ok=True)
