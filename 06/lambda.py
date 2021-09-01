"""
55: lambda expressions, map and filter functions
"""

def splicer(mystring):
    """
    splicer function
    """
    if len(mystring) % 2 == 0:
        return "EVEN"
    return mystring[0]


check_even = lambda num: num % 2 == 0
square = lambda num: num ** 2

my_nums = [1, 2, 3, 4, 5, 6]
print(list(map(square, my_nums)))
names = ["Andy", "Eve", "Sally"]
print(list(map(splicer, names)))
print(list(map(lambda x: x[0], names)))
print(list(filter(check_even, my_nums)))
print(square(3))
