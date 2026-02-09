import os
from PyPDF2 import PdfReader  # pyright: ignore[reportMissingImports]
import docx  # pyright: ignore[reportMissingImports]
from utils.config import PDF_DIR, DOC_DIR
# from utils.config import LABVIEW_DIR   # -------- DRDO MODE (UNCOMMENT) --------

from utils.chunking import chunk_text
from utils.logging import get_logger

logger = get_logger()


def read_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        logger.error(f"Error reading PDF {file_path}: {e}")
    return text


def read_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        logger.error(f"Error reading DOCX {file_path}: {e}")
    return text


# -------- DRDO MODE (TXT / LOG FILES FOR LABVIEW) --------
# def read_txt(file_path):
#     text = ""
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             text = f.read()
#     except Exception as e:
#         logger.error(f"Error reading TXT {file_path}: {e}")
#     return text


def ingest_all_docs():
    all_chunks = []

    # ---------------- PDFs ----------------
    for pdf_file in os.listdir(PDF_DIR):
        if pdf_file.endswith(".pdf"):
            path = os.path.join(PDF_DIR, pdf_file)
            text = read_pdf(path)
            all_chunks.extend(chunk_text(text))

    # ---------------- DOCX ----------------
    for doc_file in os.listdir(DOC_DIR):
        if doc_file.endswith(".docx"):
            path = os.path.join(DOC_DIR, doc_file)
            text = read_docx(path)
            all_chunks.extend(chunk_text(text))

    # ---------------- DRDO MODE ----------------
    # Supports: labview/*.txt or *.log files
    #
    # for file in os.listdir(LABVIEW_DIR):
    #     if file.endswith(".txt") or file.endswith(".log"):
    #         path = os.path.join(LABVIEW_DIR, file)
    #         text = read_txt(path)
    #         all_chunks.extend(chunk_text(text))

    logger.info(f"Ingested total {len(all_chunks)} chunks")
    return all_chunks


if __name__ == "__main__":
    chunks = ingest_all_docs()
    print(f"Total chunks ingested: {len(chunks)}")
