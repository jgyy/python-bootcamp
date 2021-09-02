"""
72. Object Oriented Programming - Special (Magic/Dunder) Methods
"""


class Sample:
    """
    Class definition
    """

    def __init__(self, title="", author="", pages=""):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}."

    def __len__(self):
        return self.pages


class Book:
    """
    Class definition
    """

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}."

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object have been deleted.")


sample = Sample()
print(sample)
b = Book("Python", "Jose", 200)
print(b)
print(len(b))
del b
