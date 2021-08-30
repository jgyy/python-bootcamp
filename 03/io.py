"""
28. I/O with Basic Files in Python
"""
file = open("../tmp/myfile.txt", "w")
file.write(
    """Hello this is a text file.
This is the second line.
This is the third line."""
)
file.close()
myfile = open("../tmp/myfile.txt")
print(myfile.read())
print(myfile.read())
myfile.seek(0)
contents = myfile.read()
print(contents)
myfile.seek(0)
print(myfile.readlines())
myfile.close()

with open("../tmp/myfile.txt", encoding="UTF-8") as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open("../tmp/my_new_file.txt", "w", encoding="UTF-8") as my_new_file:
    my_new_file.write(
        """ONE ON FIRST
TWO ON SECOND
THREE ON THIRD"""
    )

with open("../tmp/my_new_file.txt", encoding="UTF-8") as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open("../tmp/my_new_file.txt", "a", encoding="UTF-8") as my_new_file:
    my_new_file.write("\nFOUR ON FOURTH")

with open("../tmp/my_new_file.txt", encoding="UTF-8") as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open("../tmp/random.txt", "w", encoding="UTF-8") as my_new_file:
    my_new_file.write("I created this file.")

with open("../tmp/random.txt", encoding="UTF-8") as f:
    print(f.read())
