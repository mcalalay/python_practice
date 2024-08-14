import random

def display(board):
    print("Here is the current board: ")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-|-|-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-|-|-")
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("============")


def place_marker(board, marker, position):
    board[position] = marker

def player_input():
    marker = " "
    while marker not in ["X", "O"]:
        marker = input("Pick X or O: ")
        if marker not in ["X", "O"]:
            print("Sorry, please only choose from 'X' or 'O'!")
    if marker == "X":
        return("X","O")
    else:
        return ("O", "X")

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark)
        or (board[4] == board[5] == board[6] == mark)
        or (board[7] == board[8] == board[9] == mark)
        or (board[7] == board[4] == board[1] == mark)
        or (board[8] == board[5] == board[2] == mark)
        or (board[9] == board[6] == board[3] == mark)
        or (board[7] == board[5] == board[3] == mark)
        or (board[9] == board[5] == board[1] == mark))

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):

    for i in range (1,10):
        if space_check(board , i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(0,10) or not space_check(board,position):
        position = int(input("Choose a position: (1-9) "))
    return position



print("Welcome to Tekken 6 Tag Team Tournament")

while True:

    the_board = [" "] *10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":

            display(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display(the_board)
                print("Player 1 Has won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = "Player 2"

        else:

            display(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display(the_board)
                print("Player 2 Has won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = "Player 1"



    # def column_choice():
    #     column = "Wrong"
    #
    #     while (column.isdigit() == False) or (column not in ["0", "1", "2"]):
    #         column = input("Please enter only a digit that is in the range of [0-2] as a column: ")
    #         if column.isdigit() == False:
    #             print("Sorry, that is not a digit!")
    #         if column not in ["1", "2", "3"]:
    #             print("Sorry, value is out of range!")
    #
    #     return int(column)
    #
    #
    # def row_choice():
    #     row = "Wrong"
    #
    #     while row not in ["a", "b", "c"]:
    #         row = input("Please enter only from [a, b, c] as a row: ")
    #         if row.isdigit() == True:
    #             print("Sorry, that is not a letter!")
    #         if row not in ["a", "b", "c"]:
    #             print("Sorry, value is out of range!")
    #
    #     if row == "a":
    #         return rowA
    #     if row == "b":
    #         return rowB
    #     else:
    #         return rowC

    # def gameon_choice():
    #     choice = "Wrong"
    #
    #     while choice not in ["Y", "N"]:
    #         choice = input("Keep playing? (Y or N): ")
    #         if choice not in ["Y", "N"]:
    #             print("Sorry, please only choose from 'Y' or 'N'!")
    #
    #     if choice == "Y":
    #         return True
    #     if choice == "N":
    #         return False