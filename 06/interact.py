"""
47: Interactions between python files
"""
from random import shuffle


def shuffle_list(mylist):
    """
    shuffle list function
    """
    shuffle(mylist)
    return mylist


def player_guess():
    """
    shuffle list function
    """
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1, 2: ")
    return int(guess)


def check_guess(mylist, guess):
    """
    shuffle list function
    """
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Wrong Guess!")
        print(mylist)


mylists = [" ", "O", " "]
shuffle_list(mylists)
INDEX = player_guess()
check_guess(mylists, INDEX)
