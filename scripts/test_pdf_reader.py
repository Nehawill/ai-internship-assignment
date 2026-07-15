from app.parser.pdf_reader import open_pdf

pdf = open_pdf("data/ct200_manual.pdf")

if pdf:
    print("PDF opened successfully!")
    print(f"Total Pages: {pdf.page_count}")
else:
    print("Failed to open PDF.")