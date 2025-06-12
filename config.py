# config.py

# === MODEL CONFIG ===
BERT_MODEL_PATH = "bert-base-uncased"  # Can replace with local or ONNX model
MISTRAL_API_URL = "https://api.openrouter.ai/v1/chat/completions"
MISTRAL_API_KEY = "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"

# === CXO CONFIG ===
CXO_OPTIONS = ["CFO", "CHRO", "COO", "CMO", "CPO", "EA"]

# === FILE PATHS ===
UPLOAD_DIR = "./data/inputs/"
OUTPUT_DIR = "./data/outputs/"
MEMORY_STORE = "./data/memory/user_memory.json"

# === FLAGS ===
DEBUG_MODE = True
ENABLE_MULTILINGUAL = False
USE_ONNX_FALLBACK = False