import fitz  # PyMuPDF


def open_pdf(file_path: str):
    """
    Opens a PDF and returns the document object.
    """
    try:
        document = fitz.open(file_path)
        return document
    except Exception as error:
        print(f"Error opening PDF: {error}")
        return None