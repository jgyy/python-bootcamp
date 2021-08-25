def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    while True:
        choice = input("Please enter a number (0-10): ")
        if choice.isdigit() == False:
            print("Sorry that is not a number!")
        elif not (0 <= int(choice) <= 10):
            print("The number is out of range!")
        elif 0 <= int(choice) <= 10:
            return int(choice)


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
row2[1] = "X"
display(row1, row2, row3)
result = user_choice()
print(result)
