"""
131. Working with PDF Files in Python
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

if __name__ == "__main__":
    with open("../tmp/Working_Business_Proposal.pdf", "rb") as file:
        pdf_text = []
        pdf_reader = PdfFileReader(file)
        page_one = pdf_reader.getPage(1)
        for num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(num)
            pdf_text.append(page.extractText())
        print(pdf_text)
    with open("../tmp/Some_BrandNew_Doc.pdf", "wb") as file:
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(page_one)
        pdf_writer.write(file)
