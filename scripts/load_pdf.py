from app.parser.pdf_reader import (
    open_pdf,
    build_sections,
)

from app.services.document_service import save_sections

pdf = open_pdf("data/ct200_manual.pdf")

sections = build_sections(pdf)

save_sections(sections,version="v1")

print("Document stored successfully!")