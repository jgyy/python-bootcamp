def printer():
    x = 50
    return x


def greet():
    name = "Sammy"

    def hello():
        print(f"Hello {name}")

    hello()


def func():
    global x
    print(f"X is {x}")
    x = 200
    print(f"I just locally changed X to {x}")


x = 25
print(printer())
name = "THIS IS A GLOBAL STRING"
greet()
func()
print(x)
