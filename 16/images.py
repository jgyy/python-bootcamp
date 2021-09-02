"""
126. Working with Images with Python
"""
from PIL import Image

if __name__ == "__main__":
    # Use mac.show() to view the image.
    mac = Image.open("../tmp/example.jpg")
    print(mac.size)
    print(mac.format_description)
    print(mac.crop((0, 0, 100, 100)))
    pencils = Image.open("../tmp/pencils.jpg")
    print(pencils.size)
    print(pencils.format_description)
    print(pencils.crop((0, 0, 650, 130)))
    print(pencils.crop((0, 1100, 650, 1300)))
    computer = mac.crop((800, 800, 1200, 1257))
    mac.paste(im=computer, box=(0, 0))
    mac.resize((3000, 500))
    mac.rotate(90)
    red = Image.open("../tmp/red_color.jpg")
    blue = Image.open("../tmp/blue_color.png")
    blue.putalpha(128)
    red.putalpha(128)
    blue.paste(im=red, box=(0, 0), mask=red)
    blue.save("../tmp/purple.png")
