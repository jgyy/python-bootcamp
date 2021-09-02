"""
Money changing function
"""
import math


def greedy_money_exchange(denom, amount):
    """
    greedy money exchange function
    """
    i = 0
    used = [0] * len(denom)
    while amount > 0:  # go until all money gone
        # get num of that denom to use, always round down
        num = math.floor(amount / denom[i])
        used[i] = num  # say we've used it
        amount = amount - num * denom[i]  # set new amount
        i = i + 1  # go to next denom
    return used


print(greedy_money_exchange([1], 9999))
