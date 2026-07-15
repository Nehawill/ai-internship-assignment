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


def extract_text(document):
    """
    Extracts text from all pages of the PDF.
    """
    extracted_text = []

    for page_number in range(document.page_count):
        page = document.load_page(page_number)
        text = page.get_text()

        extracted_text.append({
            "page": page_number + 1,
            "text": text
        })

    return extracted_text
def extract_blocks(document):
    """
    Extract text blocks from each page while preserving layout information.
    """
    pages = []

    for page_number in range(document.page_count):
        page = document.load_page(page_number)

        blocks = page.get_text("blocks")

        page_blocks = []

        for block in blocks:
            page_blocks.append({
                "text": block[4].strip(),
                "bbox": block[:4]
            })

        pages.append({
            "page": page_number + 1,
            "blocks": page_blocks
        })

    return pages