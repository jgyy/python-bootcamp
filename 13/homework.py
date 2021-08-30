"""
101. Generators Homework Overview
"""
from random import randint


def gensquares(nums):
    """
    Create a generator that generates the squares of numbers up to some number
    """
    for num in range(nums):
        yield num ** 2


def rand_num(low, high, iteration):
    """
    Create a generator that yields "n" random numbers between a low and high number.
    """
    for _ in range(iteration):
        yield randint(low, high)


if __name__ == "__main__":
    for square in gensquares(10):
        print(square)
    for number in rand_num(1, 10, 12):
        print(number)
    STR = 'hello'
    iter_str = iter(STR)
    print(next(iter_str))
    print(next(iter_str))

    my_list = [1,2,3,4,5]
    gencomp = (item for item in my_list if item > 3)
    for item in gencomp:
        print(item)
