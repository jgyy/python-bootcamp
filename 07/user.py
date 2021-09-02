"""
63: Simple user interaction
"""

def display_game(game_lists):
    """
    display game function
    """
    print("Here is the current list: ")
    print(game_lists)


def position_choice():
    """
    display game function
    """
    choice = ""
    while choice not in ("0", "1", "2"):
        choice = input("Pick a position (0,1,2): ")
        if choice not in ("0", "1", "2"):
            print("Sorry! Invalid choice!")
    return int(choice)


def replacement_choice(game_lists, positions):
    """
    display game function
    """
    user_placement = input("Type a string to place at position: ")
    game_lists[positions] = user_placement
    return game_lists


def gameon_choice():
    """
    display game function
    """
    choice = ""
    while choice not in ("Y", "N"):
        choice = input("Keep Playing? (Y or N): ").upper()
        if choice not in ("Y", "N"):
            print("Sorry, I don't understand, please choose Y or N")
    return choice == "Y"


if __name__ == "__main__":
    GAMEON = True
    game_list = [0, 1, 2]
    while GAMEON:
        display_game(game_list)
        POSITION = position_choice()
        game_list = replacement_choice(game_list, POSITION)
        display_game(game_list)
        GAMEON = gameon_choice()
