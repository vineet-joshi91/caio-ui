import os
from dotenv import load_dotenv
load_dotenv()

# === MODEL CONFIG ===
BERT_MODEL_PATH = "bert-base-uncased"  # Adjust if you use a custom model

MISTRAL_API_URL = "https://api.openrouter.ai/v1/chat/completions"
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
if MISTRAL_API_KEY is None:
    raise ValueError("MISTRAL_API_KEY environment variable not set!")

# === CXO CONFIG ===
CXO_OPTIONS = ["CFO", "CHRO", "COO", "CMO", "CPO", "EA"]

# === APP MODES ===
DEBUG_MODE = True  # Set to False in production for less logging
ENABLE_MULTILINGUAL = False  # Set to True if you integrate language modules

# === (Add more configuration as needed for your app) ===

