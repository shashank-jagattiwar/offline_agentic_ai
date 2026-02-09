import logging
import os

from .config import VECTOR_STORE_DIR

LOG_DIR = os.path.join(VECTOR_STORE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "agent.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger():
    return logging.getLogger("AgentLogger")
