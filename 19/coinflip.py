"""
Coinflip script
"""
import random


def flip():
    """
    flip function
    """
    flips = random.random()
    return flips >= 0.5


def main(num):
    """
    wrapper function
    """
    heads = 0
    tails = 0
    result_string = ""

    for _ in range(int(num)):
        if flip():
            heads += 1
            result_string += "H"
        else:
            tails += 1
            result_string += "T"

    print("Number of Heads: %i" % (heads))
    print("Number of Tails: %i" % (tails))
    print(result_string)


userInput = input("Please enter a number of flips: ")
main(userInput)
