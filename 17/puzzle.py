"""
132. PDFs and Spreadsheets Python Puzzle Exercise
"""
from csv import reader
from PyPDF2 import PdfFileReader
from re import search

if __name__ == "__main__":
    with open("../tmp/find_the_link.csv", encoding="utf-8") as data:
        csv_data = reader(data)
        data_lines = list(csv_data)
    link_list = []
    for row_num, data in enumerate(data_lines):
        link_list.append(data[row_num])
    print("".join(link_list))

    with open("../tmp/Find_the_Phone_Number.pdf", "rb") as data:
        pdf = PdfFileReader(data)
        print(pdf.numPages)
        PATTERN = r"\d{3}.\d{3}.\d{4}"
        for num in range(pdf.numPages):
            page = pdf.getPage(num)
            page_text = page.extractText()
            match = search(PATTERN, page_text)
            if match:
                print(match.group())
