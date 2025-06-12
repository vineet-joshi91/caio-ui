# core_ai/extractor/extractor.py

import re
import spacy

# Load spaCy model (English for now)
nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str) -> dict:
    try:
        doc = nlp(text)

        entities = {
            "ORG": [],
            "PERSON": [],
            "DATE": [],
            "MONEY": [],
            "PERCENT": [],
            "KEY_METRICS": []
        }

        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent.text)

        # Custom rule-based pattern for financial metrics
        custom_metrics = re.findall(r"(?i)(revenue|profit|cost|margin|budget|expenses)\s*[:\-]?\s*\$?\₹?\d+[.,]?\d*\w*", text)
        entities["KEY_METRICS"].extend(custom_metrics)

        return entities

    except Exception as e:
        return {"error": str(e)}
