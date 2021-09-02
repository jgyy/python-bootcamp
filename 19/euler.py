""""
Find e to the Nth Digit
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go
"""
from math import e


def e_with_precision(num):
    """
    Return euler's number to the n-th decimal place

    :param n: number of decimal places to return
    :type n: int
    :return: euler's number with n decimal places
    :rtype: str
    """
    return "%.*f" % (num, e)


if __name__ == "__main__":
    # there is no do while loop in python, so we need to improvise
    CORRECT_INPUT = False
    while not CORRECT_INPUT:
        # ask until you get correct input
        print("Precision must be between 1 and 51")
        precision = int(input("Number of decimal places: "))
        if 51 >= precision > 0:
            CORRECT_INPUT = True
    print(e_with_precision(precision))
