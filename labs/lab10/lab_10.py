"""
Michael Blanco Chavez
lab_10.py

Certification of Authenticity:
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    board = build_board()
    print("{0} {1} {2}".format(board[0], board[1], board[2]))
    print("{0} {1} {2}".format(board[3], board[4], board[5]))
    print("{0} {1} {2}".format(board[6], board[7], board[8]))


def fill_spot(board, pos, char):
    if board[pos - 1] == "X" or board[pos - 1] == "0":
        return " "
    else:
        board[pos - 1] = char


def is_legal(board, position):
    return board[position] == '#'


def game_won(board):
    if board[0] == board[1] == board[2] == "O" or "X":
        return True
    if board[3] == board[4] == board[5] == "O" or "X":
        return True
    if board[6] == board[7] == board[8] == "O" or "X":
        return True
    if board[0] == board[3] == board[6] == "O" or "X":
        return True
    if board[1] == board[4] == board[7] == "O" or "X":
        return True
    if board[2] == board[5] == board[8] == "O" or "X":
        return True
    if board[0] == board[4] == board[8] == "O" or "X":
        return True
    if board[2] == board[4] == board[6] == "O" or "X":
        print("you won")
        return True
    else:
        return False


def game_over(board):
    if game_won(board):
        return True
    elif board[:] != int:
        return True
    else:
        return False


def player_input():
    player1 = input("Please pick a marker 'X' or 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Please pick a marker 'X' or 'O' ")

def play_game():
    board = build_board()
    display_board(board)
    acc = 0
    while acc != 9:
        player_input()
        pos = eval(input("enter a position"))
        if char == "X":
            fill_spot(board, pos, char)
            is_legal(board, pos)
            game_won(board)
            game_over(board)
        elif char == "Y":
            fill_spot(board, pos, char)
            is_legal(board, pos)
            game_won(board)
            game_over(board)


def main():
    play_game()


if __name__ == '__main__':
    main()
