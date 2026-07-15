from app.parser.pdf_reader import (
    open_pdf,
    extract_blocks,
    is_heading
)

pdf = open_pdf("data/ct200_manual.pdf")

pages = extract_blocks(pdf)

print("\nPage 1\n")

for block in pages[0]["blocks"]:

    if not block["text"]:
        continue

    if is_heading(block["text"]):
        print(f"HEADING  : {block['text']}")
    else:
        print(f"TEXT     : {block['text'][:60]}")