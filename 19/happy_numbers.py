"""
happy numbers script
"""


def get_digits(number):
    """
    get digits function
    """
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits


def is_happy_number(number):
    """
    check if the numner is happy
    """
    previous_numbers = []
    while True:
        digits = get_digits(number)
        sum_of_squared_digits = sum(list(map(lambda x: x ** 2, digits)))
        if sum_of_squared_digits == 1:
            return True
        if sum_of_squared_digits in previous_numbers:
            return False
        number = sum_of_squared_digits
        previous_numbers.append(number)


def print_happy_number(number):
    """
    print happy number function
    """
    happy_numbers = []
    count = 0
    while count < 8:
        if is_happy_number(number):
            happy_numbers.append(number)
            count += 1
        number += 1
    return happy_numbers


print(print_happy_number(int(input("Enter a number: "))))
