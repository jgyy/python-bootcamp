"""
problem description : program to find the factorial
values of numbers for some given number of inputs
"""


def fac(num):
    """
    factorial function
    """
    if num in [0, 1]:
        return 1
    return num * fac(num - 1)


t = int(input("Enter a number: "))
while t:
    t = t - 1
    n = int(input("Enter a number: "))
    p = fac(n)
    print(p)
