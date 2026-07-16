import sys

from app.parser.pdf_reader import (
    open_pdf,
    build_sections,
)

from app.services.document_service import save_sections

if len(sys.argv) != 3:
    print("Usage:")
    print("python -m scripts.load_pdf <pdf_path> <version>")
    sys.exit()

pdf_path = sys.argv[1]
version = sys.argv[2]

pdf = open_pdf(pdf_path)

sections = build_sections(pdf)

save_sections(sections, version)

print(f"{version} stored successfully!")