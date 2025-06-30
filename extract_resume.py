import PyPDF2
import sys

def extract_pdf_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_path = "Krish_Chaudhary_Internship_2026.pdf"
    text = extract_pdf_text(pdf_path)
    if text:
        print("=== RESUME CONTENT ===")
        print(text)
    else:
        print("Failed to extract text from PDF") 