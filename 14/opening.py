"""
105. Opening and Reading Files and Folders (Python OS Module)
"""
from os import getcwd, listdir, walk
from shutil import move
from send2trash import send2trash

if __name__ == "__main__":
    with open("../tmp/practice.txt", "w+", encoding="utf-8") as file:
        file.write("This is a test string")
    print(getcwd())
    print(listdir("/"))
    move("../tmp/practice.txt", "../tmp/practice-move.txt")
    send2trash("../tmp/practice-move.txt")
    for folder, sub_folders, files in walk(".."):
        SUBFOLDER = ""
        FILE = ""
        for sub_fold in sub_folders:
            if not SUBFOLDER:
                SUBFOLDER = "The subfolders are: \n"
            SUBFOLDER += f"    Subfolder: {sub_fold} \n"
        for file in files:
            if not FILE:
                FILE = "The files are: \n"
            FILE += f"    File: {file} \n"
        print(f"Currently looking at {folder} \n {SUBFOLDER} \n {FILE}")
