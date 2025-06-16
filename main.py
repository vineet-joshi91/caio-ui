import os
from config import (
    BERT_MODEL_PATH, CXO_OPTIONS,
    DEBUG_MODE, ENABLE_MULTILINGUAL
)

# === MVP LAUNCH: Fallback to Simple Classifier to avoid memory issues ===
USE_SIMPLE = os.environ.get("USE_SIMPLE_CLASSIFIER", "false").lower() == "true"

if USE_SIMPLE:
    from core_ai.classifier.simple_classifier import classify_document
else:
    # from core_ai.classifier.document_classifier import classify_document
    pass  # (Un-comment the above line for full ML when infra allows)

from core_ai.summarizer.cxosummary import generate_summary
from utils.universal_parser import extract_text
from core_ai.extractor.extractor import extract_entities

def process_document(file_path: str, selected_cxo: str) -> str:
    try:
        print(f"[INFO] Loading document: {file_path}")

        # Use universal parser
        file_content = extract_text(file_path)

        # Save as .txt for classifier compatibility
        temp_txt_path = file_path.rsplit(".", 1)[0] + ".txt"
        with open(temp_txt_path, "w", encoding="utf-8") as f:
            f.write(file_content)

        # === Classify document type (MVP: uses simple_classifier) ===
        doc_type = classify_document(temp_txt_path)
        print(f"[INFO] Classified as: {doc_type}")

        # 🔍 Extract key entities
        extracted_data = extract_entities(file_content)
        print(f"[INFO] Extracted Entities: {extracted_data}")

        # Generate CXO-style summary
        summary = generate_summary(temp_txt_path, cxo=selected_cxo, doc_type=doc_type)
        return summary

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return "Error processing document."

# === END: Memory-guarded MVP version ===
