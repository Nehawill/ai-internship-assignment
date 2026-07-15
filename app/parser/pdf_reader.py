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
import re


def is_heading(text: str) -> bool:
    

    pattern = r"^\d+(\.\d+)*\.?\s+.+"

    return bool(re.match(pattern, text.strip()))
def get_heading_level(heading: str) -> int:
    

    number = heading.split()[0]
    number = number.rstrip(".")

    return number.count(".") + 1
def build_sections(document):
    """
    Build a list of document sections.
    """

    pages = extract_blocks(document)

    sections = []
    current_section = None

    for page in pages:

        for block in page["blocks"]:

            text = block["text"].strip()

            if not text:
                continue

            if is_heading(text):

                if current_section:
                    sections.append(current_section)

                current_section = {
                    "title": text,
                    "level": get_heading_level(text),
                    "page": page["page"],
                    "content": []
                }

            else:

                if current_section:
                    current_section["content"].append(text)

    if current_section:
        sections.append(current_section)

    return sections