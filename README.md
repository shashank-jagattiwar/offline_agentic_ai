Offline Agentic AI Framework (FAISS + TinyLLaMA + Ollama)

This project is a fully offline Agentic AI system that:

Ingests PDFs & text documents

Builds a FAISS vector index

Uses local embeddings

Queries a local LLM (TinyLLaMA via Ollama)

Provides a GUI interface to interact with documents

Designed to run in restricted / low-internet environments (e.g. DRDO systems).

1. System Requirements
Minimum Hardware

OS: Windows 10 / 11 (64-bit)

RAM: 8 GB minimum (16 GB recommended)

CPU: x64 processor

Disk Space: ~15–20 GB free

Software

Python: 3.10 or 3.11 (recommended 3.10)

Git

Internet: Required only for initial setup 

2. Project Structure
offline_agentic_AI_framework/
│
├── agentic_env/                 # Python virtual environment
│
├── agents/
│   └── router.py
│
├── app/
│   ├── app.py
│   └── gui_app.py               # Streamlit GUI logic
│
├── data/
│   ├── docs/                    # .txt documents
│   │   └── sample.txt
│   ├── pdfs/                    # PDF documents
│   │   └── introduction to java programming.pdf
│   └── labview_txt/
│
├── models/
│   ├── embedding_models.py
│   └── llm_ollama.py             # Ollama LLM connector
│
├── scripts/
│   ├── build_index.py            # Build FAISS index
│   ├── ingest_docs.py            # Load + chunk documents
│   ├── query_engine.py           # Query pipeline
│   └── retriever.py
│
├── utils/
│   ├── config.py                 # Paths & constants
│   ├── loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── db.py
│   └── logging.py
│
├── vector_store/
│   └── faiss_index/
│       ├── index.faiss
│       └── metadata.pkl
│
├── .env
├── main.py
├── run_gui.py                    # Entry point for GUI
├── requirements.txt
└── README.md

3. Clone Project from GitHub
git clone <YOUR_GITHUB_REPO_URL>
cd offline_agentic_AI_framework

4. Create & Activate Virtual Environment
python -m venv agentic_env

Activate (Windows)
agentic_env\Scripts\activate


You should see:

(agentic_env)

5. Install All Required Libraries (ONE COMMAND)



pip install \
altair==6.0.0 annotated-types==0.7.0 anyio==4.12.1 attrs==25.4.0 blinker==1.9.0 \
cachetools==6.2.6 certifi==2026.1.4 charset-normalizer==3.4.4 click==8.3.1 \
colorama==0.4.6 faiss-cpu==1.13.2 filelock==3.20.3 fsspec==2026.2.0 \
gitdb==4.0.12 GitPython==3.1.46 h11==0.16.0 hf-xet==1.2.0 httpcore==1.0.9 \
httpx==0.28.1 huggingface_hub==1.4.1 idna==3.11 Jinja2==3.1.6 joblib==1.5.3 \
jsonschema==4.26.0 jsonschema-specifications==2025.9.1 lxml==6.0.2 \
MarkupSafe==3.0.3 mpmath==1.3.0 narwhals==2.16.0 networkx==3.6.1 \
numpy==2.4.2 ollama==0.6.1 packaging==26.0 pandas==2.3.3 pillow==12.1.0 \
protobuf==6.33.5 pyarrow==23.0.0 pydantic==2.12.5 pydantic_core==2.41.5 \
pydeck==0.9.1 pypdf==6.6.2 PyPDF2==3.0.1 python-dateutil==2.9.0.post0 \
python-docx==1.2.0 python-dotenv==1.2.1 pytz==2025.2 PyYAML==6.0.3 \
referencing==0.37.0 regex==2026.1.15 requests==2.32.5 rpds-py==0.30.0 \
safetensors==0.7.0 scikit-learn==1.8.0 scipy==1.17.0 sentence-transformers==5.2.2 \
shellingham==1.5.4 six==1.17.0 smmap==5.0.2 streamlit==1.54.0 sympy==1.14.0 \
tenacity==9.1.3 threadpoolctl==3.6.0 tokenizers==0.22.2 toml==0.10.2 \
torch==2.10.0 tornado==6.5.4 tqdm==4.67.3 transformers==5.1.0 typer-slim==0.21.1 \
typing_extensions==4.15.0 typing-inspection==0.4.2 tzdata==2025.3 \
urllib3==2.6.3 watchdog==6.0.0

6. Install & Setup Ollama (Local LLM Runtime)
Download Ollama

https://ollama.com/download

Verify Installation
ollama --version

Pull TinyLLaMA (Lightweight, Offline Friendly)
ollama pull tinyllama


Run test:

ollama run tinyllama


If it responds → LLM is working offline ✅

7. Add Your Documents

PDFs → data/pdfs/

Text files → data/docs/

Example:

data/pdfs/introduction to java programming.pdf
data/docs/sample.txt

8. Build FAISS Index (VERY IMPORTANT)

This step converts documents into embeddings and stores them locally.

python -m scripts.build_index


Expected output:

[INFO] Loaded X documents
[INFO] FAISS index created successfully


Files generated:

vector_store/faiss_index/index.faiss
vector_store/faiss_index/metadata.pkl

9. Run the GUI Application
python run_gui.py


OR

streamlit run app/gui_app.py


Browser will open automatically:

http://localhost:8501

10. How the System Works (Simple Explanation)

Documents are read & chunked

Chunks → vector embeddings

Stored in FAISS (offline)

User asks a question in GUI

Relevant chunks are retrieved

TinyLLaMA generates short, relevant answers

No internet required after setup

---------------------------------------------------------------------------------------------------

📂 Supported Data Formats (Including LabVIEW)

This project is designed to work with text-based technical documents for offline AI-powered question answering.

✅ Fully Supported Formats

The following formats work out-of-the-box without any code changes:

PDF files (.pdf)

Word documents (.docx) – including tabular data

Text files (.txt)

CSV files (.csv)

LabVIEW Measurement files (.lvm)

These files should be placed inside the appropriate data/ subfolders and indexed using:

python -m scripts.build_index

⚠️ LabVIEW Binary Files (.vi, .tdms)

Raw LabVIEW program and measurement files are binary and cannot be directly processed by language models.

Recommended approach:

Export LabVIEW data into one of the supported text formats:

.csv

.txt

.lvm

.pdf

This export is a standard feature in LabVIEW and preserves all meaningful data required for AI-based analysis.

🔧 Optional Extension (TDMS Support)

If .tdms files must be used directly, they can be converted using:

pip install nptdms


After conversion to text or CSV, the data can be indexed normally.

🧠 Why This Approach?

The system is optimized for:

Technical reports

Parameter tables

Experimental summaries

Documentation and logs

Language models operate on textual information, making exported LabVIEW data ideal for accurate and relevant answers.