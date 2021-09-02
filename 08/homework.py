"""
73. Object Oriented Programming - Homework
"""
from math import pi


class Line:
    """
    defining a class
    """

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.xxx = coor2[0] - coor1[0]
        self.yyy = coor2[1] - coor1[1]

    def distance(self):
        """
        class method
        """
        return (self.xxx ** 2 + self.yyy ** 2) ** 0.5

    def slope(self):
        """
        class method
        """
        return self.yyy / self.xxx


class Cylinder:
    """
    defining a class
    """

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        """
        class method
        """
        return pi * self.radius ** 2 * self.height

    def surface_area(self):
        """
        class method
        """
        return (2 * pi * self.radius * self.height) + (2 * pi * self.radius ** 2)


if __name__ == "__main__":
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)
    li = Line(coordinate1, coordinate2)
    print(li.distance())
    print(li.slope())
    c = Cylinder(2, 3)
    print(c.volume())
    print(c.surface_area())
