import os
import sys

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit.web.bootstrap as bootstrap # pyright: ignore[reportMissingImports]

if __name__ == "__main__":
    bootstrap.run(
        "app/gui_app.py",
        "",
        [],
        {}
    )
