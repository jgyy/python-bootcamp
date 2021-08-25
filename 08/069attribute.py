import math


class Dog:
    species = "mammle"

    def __init__(self, breed, name, spots=False):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}.")


class Circle:
    pi = math.pi

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius ** 2 * self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


dog = Dog("lab", "Sammy")
print(dog.species, dog.breed, dog.name, dog.spots)
dog.bark(1)
circle = Circle(10)
print(circle.pi, circle.radius, circle.area)
print(circle.get_circumference())
