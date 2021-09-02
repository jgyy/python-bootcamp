"""
69. Object Oriented Programming - Attributes and Class Keyword
"""
import math


class Dog:
    """
    DOG class
    """

    species = "mammle"

    def __init__(self, breed, name, spots=False):
        self.breed = breed
        self.name = name
        self.spots = spots

    def __call__(self):
        pass

    def bark(self, number):
        """
        bark method
        """
        print(f"WOOF! My name is {self.name} and the number is {number}.")


class Circle:
    """
    DOG class
    """

    pi = math.pi

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius ** 2 * self.pi

    def __call__(self):
        pass

    def get_circumference(self):
        """
        bark method
        """
        return self.radius * self.pi * 2


dog = Dog("lab", "Sammy")
print(dog.species, dog.breed, dog.name, dog.spots)
dog.bark(1)
circle = Circle(10)
print(circle.pi, circle.radius, circle.area)
print(circle.get_circumference())
