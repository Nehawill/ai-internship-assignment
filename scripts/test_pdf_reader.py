from app.parser.pdf_reader import (
    open_pdf,
    build_sections,
)

pdf = open_pdf("data/ct200_manual.pdf")

sections = build_sections(pdf)

for section in sections:

    print("=" * 60)
    print(f"Title : {section['title']}")
    print(f"Level : {section['level']}")
    print(f"Page  : {section['page']}")

    print("\nContent:\n")

    for paragraph in section["content"]:
        print(paragraph)