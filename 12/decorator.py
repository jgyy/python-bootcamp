"""
98: Decorators with python overview
"""


def func(name="Jose"):
    """
    function
    """
    print(f"Hello {name}!")

    def greet():
        return "\t This is the greet function inside hello"

    def welcome():
        return "\t This is the welcome function inside hello"

    print("returning function")
    return greet if name == "Jose" else welcome


def hello():
    """
    hello function
    """
    return "Hi Jose"


def other(def_func):
    """
    other function
    """
    print("other code runs here")
    print(def_func())


def new_decorator(original_func):
    """
    decorator function
    """

    def wrap_func():
        print("Code before the original function")
        original_func()
        print("Code after the original function")

    return wrap_func

@new_decorator
def func_decorated():
    """
    decorated function
    """
    print("I want to be decorated")


if __name__ == "__main__":
    function = func()
    print(function())
    other(hello)
    func_decorated()
