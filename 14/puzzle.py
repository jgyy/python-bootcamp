"""
114. Advanced Python Module Puzzle - Overview
"""
from shutil import unpack_archive
from re import findall, search
from os import walk


def func_search(file, pattern=r"\d{3}-\d{3}-\d{4}"):
    """
    Search pattern from a file
    """
    with open(file, "r", encoding="utf-8") as openfile:
        text = openfile.read()

    if search(pattern, text):
        return search(pattern, text)
    return ""


if __name__ == "__main__":
    unpack_archive("../tmp/unzip_me_for_instructions.zip", "../tmp/", "zip")
    with open("../tmp/extracted_content/Instructions.txt", encoding="utf-8") as zipfile:
        content = zipfile.read()
        print(content)
    PATTERN = r"\d{3}-\d{3}-\d{4}"
    STRING = "here is a random number 1231231234 , here is phone number formatted 123-123-1234"
    print(findall(PATTERN, STRING))

    results = []
    for folder, sub_folders, files in walk("../tmp/extracted_content"):
        print(folder, sub_folders, files)
        for f in files:
            full_path = folder + "/" + f
            results.append(func_search(full_path))
    for r in results:
        if r != "":
            print(r.group())
