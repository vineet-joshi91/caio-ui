# utils/universal_parser.py

from PyPDF2 import PdfReader
import docx

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        reader = PdfReader(pdf_path)
        full_text = ""

        for page in reader.pages:
            full_text += page.extract_text() + "\n"

        return full_text.strip()
    except Exception as e:
        return f"[PDF Error] {str(e)}"

def extract_text_from_docx(docx_path: str) -> str:
    try:
        doc = docx.Document(docx_path)
        full_text = "\n".join([para.text for para in doc.paragraphs])
        return full_text.strip()
    except Exception as e:
        return f"[DOCX Error] {str(e)}"

def extract_text_from_txt(txt_path: str) -> str:
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"[TXT Error] {str(e)}"

def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        return "[Unsupported file type]"
