from os import system
from random import randint


def display_board(board):
    # system("clear")
    display = f"""
{board[7]} | {board[8]} | {board[9]}
{"-"*9}
{board[4]} | {board[5]} | {board[6]}
{"-"*9}
{board[1]} | {board[2]} | {board[3]}
    """
    legend = f"""Legend
7 | 8 | 9
{"-"*9}
4 | 5 | 6
{"-"*9}
1 | 2 | 3
    """
    print(legend)
    print(display)


def player_input():
    marker = ""
    while marker not in ("X", "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()
    return ("X", "O") if marker == "X" else ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark)
        or (board[4] == board[5] == board[6] == mark)
        or (board[1] == board[2] == board[3] == mark)
        or (board[7] == board[4] == board[1] == mark)
        or (board[8] == board[5] == board[2] == mark)
        or (board[9] == board[6] == board[3] == mark)
        or (board[7] == board[5] == board[3] == mark)
        or (board[9] == board[5] == board[1] == mark)
    )


def choose_first():
    return "Player 2" if randint(0, 1) == 0 else "Player 1"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        print(space_check(board, i))
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in list(range(1, 10)) or not space_check(board, position):
        position = int(input("Choose your next position (1-9): "))
    return position


def replay():
    text = "Do you want to play again? Enter Yes or No: "
    return input(text).lower().startswith("y")


if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    while True:
        # Reset the board
        the_board = [" "] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + " will go first.")
        play_game = input("Are you ready to play? Enter Yes or No.")
        game_on = play_game.lower()[0] == "y"
        while game_on:
            if turn == "Player 1":
                display_board(the_board)
                print(f"{turn} turn ({player1_marker})")
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)
                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print(f"Congratulations! {turn} have won the game!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        game_on = False
                    else:
                        turn = "Player 2"
            else:
                display_board(the_board)
                print(f"{turn} turn ({player2_marker})")
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Player 2 has won!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        game_on = False
                    else:
                        turn = "Player 1"
        if not replay():
            break
