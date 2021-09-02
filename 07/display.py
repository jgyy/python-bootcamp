"""
60: Displaying information
"""


def display(row1, row2, row3):
    """
    display function
    """
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    """
    display function
    """
    while True:
        choice = input("Please enter a number (0-10): ")
        if not choice.isdigit():
            print("Sorry that is not a number!")
        elif not 0 <= int(choice) <= 10:
            print("The number is out of range!")
        elif 0 <= int(choice) <= 10:
            return int(choice)


row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]
row_2[1] = "X"
display(row_1, row_2, row_3)
result = user_choice()
print(result)
