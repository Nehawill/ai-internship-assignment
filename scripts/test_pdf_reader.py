from app.parser.pdf_reader import open_pdf, extract_blocks

pdf = open_pdf("data/ct200_manual.pdf")

if pdf:
    pages = extract_blocks(pdf)

    first_page = pages[0]

    print(f"Page {first_page['page']}")

    for block in first_page["blocks"]:
        print("=" * 50)
        print(block["text"])