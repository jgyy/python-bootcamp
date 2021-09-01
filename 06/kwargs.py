"""
49: *args and **kwargs in python
"""

def myfunc(*args, **kwargs):
    """
    function with arguments
    """
    if args:
        print(sum(args))
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")


myfunc(40, 60)
myfunc(40, 60, 100, 200)
myfunc(fruit="apple", veggie="lettuce")
