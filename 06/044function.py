def say_hello(name="Anon"):
    print(f"Hello {name}")


def add_num(num1, num2):
    return num1 + num2


def print_result(num1, num2):
    print(num1 + num2)


def myfunc(a, b):
    print(a + b)
    return a + b


say_hello()
sum = add_num(10, 20)
print(sum)
print_result(30, 40)
sum2 = myfunc(50, 60)
print(sum2)
print(add_num("10", "20"))