import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st # pyright: ignore[reportMissingImports]
from scripts.query_engine import QueryEngine

st.set_page_config(page_title="DRDO Offline AI", layout="wide")

st.title("🛰️ DRDO Offline Agentic AI Assistant")
st.caption("Secure Local Knowledge Retrieval System")

# --LOAD ENGINE ONCE -------
@st.cache_resource
def get_engine():
    return QueryEngine()

engine = get_engine()

# ----- SESSION MEMORY ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- FILE UPLOAD (PRO FEATURE) ---------
st.sidebar.header("📂 Upload Document")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF for quick testing",
    type=["pdf"]
)

if uploaded_file:
    save_path = os.path.join("data/pdfs", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())

    st.sidebar.success("Uploaded! Rebuild index to use it.")

# ---------------- QUESTION INPUT ----------------
question = st.text_input("Ask a question:")

if st.button("Ask"):

    if question.strip() != "":

        with st.spinner("🔎 Searching documents + generating answer..."):

            answer = engine.query(question)

        # Save history
        st.session_state.history.append((question, answer))

# ---------------- DISPLAY CHAT HISTORY ----------------
st.subheader("💬 Conversation")

for q, a in reversed(st.session_state.history):
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 AI:** {a}")
    st.markdown("---")
