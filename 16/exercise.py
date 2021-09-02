"""
127. Python Image Exercises - Overview
"""
from PIL import Image

if __name__ == "__main__":
    words = Image.open("../tmp/word_matrix.png")
    mask = Image.open("../tmp/mask.png")
    mask = mask.resize(words.size)
    mask.putalpha(200)
    words.paste(mask,(0,0),mask)
    words.show()
