"""
81: Error and exception homework
"""


def ask():
    """
    Ask function
    """
    while True:
        try:
            square = int(input("Enter an integer: ")) ** 2
        except TypeError:
            print("Invalid input. Please try again.")
        else:
            print(f"The square is {square}")
            break


if __name__ == "__main__":
    for i in ["a", "b", "c"]:
        try:
            print(i ** 2)
        except TypeError:
            print("Unable to power string")
    try:
        X = 5
        Y = 0
        Z = X / Y
    except ZeroDivisionError:
        print("Unable to divide by zero")
    finally:
        print("All Done.")
    ask()
