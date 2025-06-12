# main.py

import os
from config import (
    BERT_MODEL_PATH, CXO_OPTIONS,
    DEBUG_MODE, ENABLE_MULTILINGUAL
)

from core_ai.classifier.document_classifier import classify_document
from core_ai.summarizer.cxosummary import generate_summary
from utils.universal_parser import extract_text
from core_ai.extractor.extractor import extract_entities

def auto_assign_cxo(doc_type: str) -> str:
    routing_map = {
        "Finance Report": "CFO",
        "HR Feedback": "CHRO",
        "Operations Summary": "COO",
        "Marketing Campaign Report": "CMO",
        "Recruitment Strategy": "CPO",
        "Executive Overview": "EA"
    }
    return routing_map.get(doc_type, "EA")  # Default fallback to Executive Assistant

def process_document(file_path: str, user_tier: str = "Free") -> str:
    try:
        print(f"[INFO] Loading document: {file_path}")

        # Parse file content
        file_content = extract_text(file_path)

        # Save as .txt for classifier compatibility
        temp_txt_path = file_path.rsplit(".", 1)[0] + ".txt"
        with open(temp_txt_path, "w", encoding="utf-8") as f:
            f.write(file_content)

        # Classify document type
        doc_type = classify_document(temp_txt_path)
        print(f"[INFO] Classified as: {doc_type}")

        # Auto-assign CXO based on tier and document type
        if user_tier == "Free":
            selected_cxo = "EA"  # Executive Summary only
        else:
            selected_cxo = auto_assign_cxo(doc_type)
        print(f"[INFO] Auto-assigned CXO: {selected_cxo}")

        # Extract key entities (optional for Phase 1)
        extracted_data = extract_entities(file_content)
        print(f"[INFO] Extracted Entities: {extracted_data}")

        # Generate CXO summary
        summary = generate_summary(
            file_path=temp_txt_path,
            cxo=selected_cxo,
            doc_type=doc_type
        )

        return summary

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return "Error processing document."
