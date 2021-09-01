"""
56: nested statements and scope
"""

def printer():
    """
    printer function
    """
    xxx = 50
    return xxx


def greet():
    """
    printer function
    """
    name = "Sammy"

    def hello():
        print(f"Hello {name}")

    hello()


def func(xxx):
    """
    printer function
    """
    print(f"X is {xxx}")
    xxx = 200
    print(f"I just locally changed X to {xxx}")


print(printer())
greet()
func(25)
print(25)
