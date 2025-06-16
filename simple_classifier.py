# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 19:03:19 2025

@author: Vineet
"""

# core_ai/classifier/simple_classifier.py

LABELS = [
    "Finance Report",
    "HR Feedback",
    "Operations Summary",
    "Marketing Campaign Report",
    "Recruitment Strategy",
    "Executive Overview"
]

KEYWORDS = {
    "Finance Report": ["revenue", "profit", "loss", "balance sheet", "finance"],
    "HR Feedback": ["employee", "hr", "feedback", "review", "sentiment"],
    "Operations Summary": ["operations", "efficiency", "workflow", "process"],
    "Marketing Campaign Report": ["marketing", "campaign", "ad spend", "leads"],
    "Recruitment Strategy": ["recruitment", "hiring", "talent", "candidate"],
    "Executive Overview": ["overview", "summary", "executive", "c-suite"]
}

def classify_document(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().lower()
        for label, keywords in KEYWORDS.items():
            if any(kw in content for kw in keywords):
                return label
        return "Executive Overview"
    except Exception as e:
        print(f"[Simple Classifier Error] {str(e)}")
        return "Unknown Document Type"
