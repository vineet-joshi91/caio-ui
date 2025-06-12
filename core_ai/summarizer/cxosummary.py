# core_ai/summarizer/cxosummary.py

import os
import requests
from brains.persona_map import CXO_PERSONA_PROMPTS
from config import MISTRAL_API_URL, MISTRAL_API_KEY, DEBUG_MODE

def fallback_summary(file_path: str, cxo: str, doc_type: str = "") -> str:
    """Fallback template-based summary for offline/API failure mode."""
    from datetime import datetime
    cxo_templates = CXO_PERSONA_PROMPTS
    doc_type_note = f"\n[Detected Doc Type: {doc_type}]" if doc_type else ""
    return (
        cxo_templates.get(cxo, "General business document summary.") +
        f"\n\n[Automated fallback summary generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
        + doc_type_note
    )

def generate_summary(file_path: str, cxo: str, doc_type: str = "") -> str:
    try:
        # Read document content
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()

        # Use persona prompt from brains
        base_prompt = CXO_PERSONA_PROMPTS.get(
            cxo, "You are a business analyst. Summarize this document."
        )
        full_prompt = f"{base_prompt}\n\nDocument Type: {doc_type}\n\nContent:\n{file_content}"

        if DEBUG_MODE:
            print(f"\n--- Prompt Sent to LLM ---\n{full_prompt[:1000]}...\n")

        # Call Mistral (OpenRouter API)
        response = requests.post(
            MISTRAL_API_URL,
            headers={
                "Authorization": f"Bearer {MISTRAL_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral-7b",
                "messages": [
                    {"role": "system", "content": "You are a helpful and concise AI assistant."},
                    {"role": "user", "content": full_prompt}
                ]
            }
        )

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        else:
            print(f"[Error] LLM API failure: {response.status_code}\n{response.text}")
            return fallback_summary(file_path, cxo, doc_type)

    except Exception as e:
        print(f"[LLM Summarizer Error] {e}")
        return fallback_summary(file_path, cxo, doc_type)
