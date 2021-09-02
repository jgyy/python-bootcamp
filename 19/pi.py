"""
Name: pi.py
Purpose: Get the value of Pi to n number of decimal places
Algorithm: Chudnovsky Algorithm

Module Dependencies:

Math provides fast square rooting
Decimal gives the Decimal data type which is much better than Float
sys is needed to set the depth for recursion.
"""
from __future__ import print_function
import math
import sys
from decimal import getcontext, ROUND_FLOOR, Decimal

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)


def factorial(num):
    """
    Return the Factorial of a number using recursion

    Parameters:
    n -- Number to get factorial of
    """
    if not num:
        return 1
    return num * factorial(num - 1)


def get_iterated_value(num):
    """
    Return the Iterations as given in the Chudnovsky Algorithm.
    k iterations gives k-1 decimal places.. Since we need k decimal places
    make iterations equal to k+1

    Parameters:
    num  -- Number of Decimal Digits to get
    """
    num = num + 1
    getcontext().prec = num
    sums = 0
    for k in range(num):
        first = factorial(6 * k) * (13591409 + 545140134 * k)
        down = factorial(3 * k) * (factorial(k)) ** 3 * (640320 ** (3 * k))
        sums += first / down
    return Decimal(sums)


def get_value_of_pi(k):
    """
    Returns the calculated value of Pi using the iterated value of the loop
    and some division as given in the Chudnovsky Algorithm

    Parameters:
    k -- Number of Decimal Digits upto which the value of Pi should be calculated
    """
    iteration = get_iterated_value(k)
    num_up = 426880 * math.sqrt(10005)

    return Decimal(num_up) / iteration


def shell():
    """
    Console Function to create the interactive Shell.
    Runs only when __name__ == __main__ that is when the script is being called directly

    No return value and Parameters
    """
    print(
        "Welcome to Pi Calculator.",
        "In the shell below, Enter the number of digits,",
        "up to which the value of Pi should be calculated or enter quit to exit",
    )

    while True:
        print(">>> ", end="")
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("You did not enter a number. Try again")
        else:
            print(get_value_of_pi(int(entry)))


if __name__ == "__main__":
    shell()
