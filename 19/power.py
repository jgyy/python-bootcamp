"""
Enter two numbers a and b (separated by newline) and the
program will print a^b with O(log N) time complexity
"""


def pow_func(arga, argb):
    """
    Return a to the power of b
    """
    if argb == 0:
        return 1
    temp = pow_func(arga, argb / 2)
    if argb % 2 == 0:
        return temp * temp
    return temp * temp * arga


if __name__ == "__main__":
    a = int(input("Value a: "))
    b = int(input("Value b: "))
    print(pow_func(a, b))
