from random import randint
from os import system 

def init_board():
    return [[0, 0, 0] for i in range(3)]

def get_move(board: list, player: list):
    alpha = ['A', 'B', 'C']
    player_name = 'X' if player == 1 else 'O'
    move = input("\n{}\'s move: ".format(player_name)).upper()
    if move == "QUIT":
        print("\nQuit")
        exit()
    if re.fullmatch(r'[A-C][1-3]', move):
        row = alpha.index(move[:1])
        col = int(move[1:]) - 1
        if board[row][col] == 0:
            return row, col
    print("Wrong input!")
    return get_move(board, player)

def get_ai_move(board, player):
    row, col = 0, 0
    return row, col

def mark(board, player, row, col):
    board[row][col] = player

def has_won(board, player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        elif board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True
    

def print_board(board):
    head = 2*' ' + '1' + 3*' ' + '2' + 3*' ' + '3' + '\n'
    print('\n', head)
    inter_row = (11*" " + "\n" + 2*' ' + 3*"-" + "+" + 3*"-" + "+" + 3*"-" + "\n" + 11 * " ")
    for i in range(len(board)):
        if i == 0:
            row_sign = 'A '
        elif i == 1:
            row_sign = 'B '
        else:
            row_sign = 'C '
        print(row_sign, board[i][0], '|', board[i][1], '|', board[i][2])
        if i < len(board)-1:
            print(inter_row)
    print('\n')


def print_result(player):
    if player == 0:
        print("\nThe game is a tie!")
    elif player == 1:
        print("\nX has won the game!")
    elif player == 2:
        print("\nO has won the game!")

def huvshu():
    board = init_board()
    player = randint(1,2)

    while True:
        print_board(board)
        row, col = get_move(board,player)
        mark(board,player,row,col)
        if has_won(board,player):
            print_result(player)
            break
        elif  is_full(board):
            print_result(0)
            break
        player == 2 if player == 1 else 1
    system('clear')
    print_board(board)


def tictactoe_game(mode='HUMAN-HUMAN'):
    huvshu()

def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
