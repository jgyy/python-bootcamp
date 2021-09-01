"""
44: Basics of python functions
"""

def say_hello(name="Anon"):
    """
    say hello function
    """
    print(f"Hello {name}")


def add_num(num1, num2):
    """
    say hello function
    """
    return num1 + num2


def print_result(num1, num2):
    """
    say hello function
    """
    print(num1 + num2)


def myfunc(a, b):
    """
    say hello function
    """
    print(a + b)
    return a + b


say_hello()
SUMS = add_num(10, 20)
print(SUMS)
print_result(30, 40)
SUM2 = myfunc(50, 60)
print(SUM2)
print(add_num("10", "20"))
