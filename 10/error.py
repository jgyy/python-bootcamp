"""
80: Errors and Exception Handling
"""


def add(num_1, num_2):
    """
    Addition function
    """
    try:
        answer = num_1 + num_2
    except TypeError:
        print("Hey, it looks like you are not adding correctly!")
    else:
        print("Add went well!")
        print(answer)


def file():
    """
    Open File function
    """
    try:
        with open("../tmp/testfile", "w", encoding="utf-8") as open_file:
            open_file.write("Write a test line")
    except TypeError:
        print("There was a type error!")
    except OSError:
        print("Hey you have a OS Error")
    finally:
        print("I always run.")


def ask_for_int():
    """
    Asking for integer input
    """
    while True:
        try:
            result = int(input("Please provide number: "))
        except TypeError:
            print("Whoops! That is not a number.")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally.")
    return result


if __name__ == "__main__":
    NUM_1 = 10
    NUM_2 = 20
    add(NUM_1, NUM_2)
    file()
    ask_for_int()
