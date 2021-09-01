"""
57: Methods and Functions Overview Homework
"""

from math import pi
from string import ascii_lowercase

# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as (4 / 3) * π * (r ** 3)
def vol(rad):
    """
    calculate the volume of sphere
    """
    return (4 / 3) * pi * (rad ** 3)


print(vol(2))

# Write a function that checks whether a number
# is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    """
    calculate the volume of sphere
    """
    if low <= num <= high:
        return f"{num} is in the range between {low} and {high}"
    return f"{num} is NOT in the range between {low} and {high}"


print(ran_check(5, 2, 7))

# If you only wanted to return a boolean:
def ran_bool(num, low, high):
    """
    calculate the volume of sphere
    """
    return low <= num <= high


print(ran_bool(3, 1, 10))

# Write a Python function that accepts a string and calculates
# the number of upper case letters and lower case letters.
def up_low(sss):
    """
    calculate the volume of sphere
    """
    upper = 0
    lower = 0
    for letter in sss:
        if letter.isupper():
            upper += 1
        if letter.islower():
            lower += 1
    return "\n".join(
        [
            f"No. of Upper case characters: {upper}",
            f"No. of Lower case Characters: {lower}",
        ]
    )


s = "Hello Mr. Rogers, how are you this fine Tuesday?"
print(up_low(s))

# Write a Python function that takes a list and returns
# a new list with unique elements of the first list.
def unique_list(lst):
    """
    calculate the volume of sphere
    """
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

# Write a Python function to multiply
# all the numbers in a list.
def multiply(numbers):
    """
    calculate the volume of sphere
    """
    multi = 1
    for num in numbers:
        multi *= num
    return multi


print(multiply([1, 2, 3, -4]))

# Write a Python function that checks whether
# a word or phrase is palindrome or not.
def palindrome(sss):
    """
    calculate the volume of sphere
    """
    return sss == sss[::-1]


print(palindrome("helleh"))

# Write a Python function to check whether
# a string is pangram or not.
def ispangram(str1, alphabet=ascii_lowercase):
    """
    calculate the volume of sphere
    """
    str_list = list(str1.lower())
    string = set(list(filter(lambda x: x in alphabet, str_list)))
    return len(string) == len(alphabet)


print(ispangram("The quick brown fox jumps over the lazy dog"))
