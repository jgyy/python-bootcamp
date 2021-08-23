def even_check(number):
    result = number % 2 == 0
    return result


def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print(even_check(21))
print(even_check(22))
print(check_even_list([1, 2, 3, 4]))
print(check_even_list([1, 3, 5, 7]))
