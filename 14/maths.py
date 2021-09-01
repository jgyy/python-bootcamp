"""
107: Python Math and Random Modules
"""
from math import pi, e, inf, nan, log, sin, floor, ceil, degrees, radians
from random import randint, seed, choice, choices, sample, shuffle, uniform, gauss

if __name__ == "__main__":
    print(pi, e, inf, nan)
    print(floor(4.35))
    print(ceil(4.35))
    print(round(2.5))
    print(log(9999, 9))
    print(sin(99))
    print(degrees(pi * pi))
    print(radians(999))
    seed(randint(1, 9999))
    print(randint(1, 9999))
    mylist = list(range(0, 9999))
    print(choice(mylist))
    print(choices(mylist, k=9))
    print(sample(mylist, k=9))
    shuffle(mylist)
    print(mylist[:9])
    print(uniform(0, 100))
    print(gauss(0, 1))
