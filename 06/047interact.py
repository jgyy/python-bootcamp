from math import e
from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1, 2: ")
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Wrong Guess!")
        print(mylist)


mylist = [" ", "O", " "]
shuffle_list(mylist)
myindex = player_guess()
check_guess(mylist, myindex)
