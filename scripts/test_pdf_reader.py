from app.parser.pdf_reader import open_pdf, extract_text

pdf = open_pdf("data/ct200_manual.pdf")

if pdf:
    print("PDF opened successfully!")
    print(f"Total Pages: {pdf.page_count}")

    pages = extract_text(pdf)

    print("\n----- First Page Preview -----\n")
    print(pages[0]["text"][:1000])   # Print first 1000 characters only

else:
    print("Failed to open PDF.")