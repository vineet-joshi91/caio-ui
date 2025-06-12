# core_ai/classifier/document_classifier.py

from transformers import pipeline

# Define labels for your document types / CXO categories
LABELS = [
    "Finance Report",
    "HR Feedback",
    "Operations Summary",
    "Marketing Campaign Report",
    "Recruitment Strategy",
    "Executive Overview"
]

# Load zero-shot classifier using DistilBERT or BART
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_document(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        result = classifier(content, candidate_labels=LABELS)
        best_label = result["labels"][0]
        return best_label

    except Exception as e:
        print(f"[Classifier Error] {str(e)}")
        return "Unknown Document Type"
