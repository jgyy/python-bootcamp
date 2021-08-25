from math import pi


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x = coor2[0] - coor1[0]
        self.y = coor2[1] - coor1[1]

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def slope(self):
        return self.y / self.x


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return pi * self.radius ** 2 * self.height

    def surface_area(self):
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
