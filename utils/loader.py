import os
import docx  # pyright: ignore[reportMissingImports]
from pypdf import PdfReader  # pyright: ignore[reportMissingImports]

from utils.config import PDF_DIR, DOC_DIR
# from utils.config import LABVIEW_DIR   # ← UNCOMMENT AT DRDO


def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()


def load_docx(path):
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


# -------- FUTURE: LABVIEW TXT/LOG READER --------
# def load_txt(path):
#     try:
#         with open(path, "r", encoding="utf-8", errors="ignore") as f:
#             return f.read().strip()
#     except:
#         return ""


def load_documents():
    documents = []

    # ---------- PDFs ----------
    for file in os.listdir(PDF_DIR):
        if file.lower().endswith(".pdf"):
            path = os.path.join(PDF_DIR, file)
            text = load_pdf(path)
            if text:
                documents.append(text)

    # ---------- DOCX ----------
    for file in os.listdir(DOC_DIR):
        if file.lower().endswith(".docx"):
            path = os.path.join(DOC_DIR, file)
            try:
                text = load_docx(path)
                if text:
                    documents.append(text)
            except Exception:
                print(f"[WARN] Skipping invalid DOCX: {file}")

    # ---------- LABVIEW FILES (ENABLE AT DRDO) ----------
    #
    # if os.path.exists(LABVIEW_DIR):
    #     for file in os.listdir(LABVIEW_DIR):
    #         if file.lower().endswith((".txt", ".log", ".vi")):
    #             path = os.path.join(LABVIEW_DIR, file)
    #             text = load_txt(path)
    #             if text:
    #                 documents.append(text)

    print(f"[INFO] Loaded {len(documents)} documents")
    return documents
