"""
113. Zipping and Unzipping files with Python
"""
from zipfile import ZipFile, ZIP_DEFLATED
from shutil import make_archive, unpack_archive

if __name__ == "__main__":
    with open("../tmp/fileone.txt", "w+", encoding="utf-8") as file:
        file.write("ONE FILE")
    with open("../tmp/filetwo.txt", "w+", encoding="utf-8") as file:
        file.write("TWO FILE")
    with ZipFile("../tmp/comp_file.zip", "w") as file:
        file.write("../tmp/fileone.txt", compress_type=ZIP_DEFLATED)
        file.write("../tmp/filetwo.txt", compress_type=ZIP_DEFLATED)
    with ZipFile("../tmp/comp_file.zip", "r") as file:
        file.extractall("../tmp/extracted_content")
    make_archive("../tmp/example", "zip", "../tmp/")
    unpack_archive("../tmp/example.zip", "../tmp/final_unzip", "zip")
