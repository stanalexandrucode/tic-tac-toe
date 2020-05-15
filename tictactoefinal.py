from random import randint, choice
from os import system
import os
import time
from time import sleep
# import colorama
# from colorama import Fore, Style


def main_title():
    os.system('clear')
    print("""\             ######## ####  ######   
                 ##     ##  ##    ## 
                 ##     ##  ##       
                 ##     ##  ##          
                 ##     ##  ##       
                 ##     ##  ##    ## 
                 ##    ####  ######   """)
    time.sleep(.5)
    os.system('clear')
    print("""\             ######## ####  ######          ########    ###     ######  
                 ##     ##  ##    ##            ##      ## ##   ##    ## 
                 ##     ##  ##                  ##     ##   ##  ##       
                 ##     ##  ##       #######    ##    ##     ## ##       
                 ##     ##  ##                  ##    ######### ##       
                 ##     ##  ##    ##            ##    ##     ## ##    ## 
                 ##    ####  ######             ##    ##     ##  ######  """)
    time.sleep(.5)
    os.system('clear')
    print("""\             ######## ####  ######          ########    ###     ######          ########  #######  ######## 
                 ##     ##  ##    ##            ##      ## ##   ##    ##            ##    ##     ## ##       
                 ##     ##  ##                  ##     ##   ##  ##                  ##    ##     ## ##       
                 ##     ##  ##       #######    ##    ##     ## ##       #######    ##    ##     ## ######   
                 ##     ##  ##                  ##    ######### ##                  ##    ##     ## ##       
                 ##     ##  ##    ##            ##    ##     ## ##    ##            ##    ##     ## ##       
                 ##    ####  ######             ##    ##     ##  ######             ##     #######  ######## """)


def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    return board


def is_error(coordinates, board):
	valid_coords = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
	if coordinates not in valid_coords:
		return True
	else:
		coordinates = make_coords(coordinates)
		for i, x in enumerate(board):
			if i == int(coordinates[0]):
				if board[i][int(coordinates[1])] in ['X', 'O']:
					return True
				else:
					return False


def get_input(board, player):
	error = None
	while True:
		system('clear')
		print_board(board)
		if error != None:
			print(error)
		coordinates = input(f'\tType your Coordinates ({player}): ').lower()
		if not is_error(coordinates, board):
			break
		error = '\tInvalid input!'
	return coordinates


def get_move(player, board, coordinates):
	for i, x in enumerate(board):
		if i == int(coordinates[0]):
			board[i][int(coordinates[1])] = player
	return board


def make_coords(field):
	alpha = ['a', 'b', 'c']
	coordinates = f'{alpha.index(field[0])}{int(field[1]) - 1}'
	return coordinates


def _turn_(board, player):
	coordinates = make_coords(get_input(board, player))
	board = get_move(player, board, coordinates)
	return board, coordinates


'''def ai_turn(board, player):
	ai_coordinates = make_coords(get_ai_move(board,player))
	board = get_move(player, board, make_coords(ai_coordinates))
	return ai_coordinates'''


def get_ai_move(board, player):
	alpha = ['a', 'b', 'c']
	ai_coordinates = f'{choice(alpha)}{randint(1, 3)}'
	while True:
		if is_error(ai_coordinates, board) == False:
			board = get_move(player, board, make_coords(ai_coordinates))
			break
		else:
			ai_coordinates = f'{choice(alpha)}{randint(1, 3)}'
	return board, make_coords(ai_coordinates)


def has_won(board, x, y):
	if board[0][y] == board[1][y] == board[2][y]:
	    return True
	elif board[x][0] == board[x][1] == board[x][2]:
	    return True
	elif x == y and board[0][0] == board[1][1] == board[2][2]:
	    return True
	elif x + y == 2 and board[0][2] == board[1][1] == board[2][0]:
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


def print_result(winner):
	if winner == None:
		input('It\'s tie.')
	else:
		input(f'\n\tWinner is {winner}!')


def huvshu(p_one, p_two):
	board = init_board()
	player_one = 'O'
	player_two = 'X'
	for turn in range(9):
		if turn % 2 != 0:
			board, coordinates = _turn_(board, player_one)
			if has_won(board, int(coordinates[0]), int(coordinates[1])) == True:
				system('clear')
				print_board(board)
				return p_one
			turn += 1
		else:
			board, coordinates = _turn_(board, player_two)
			if has_won(board, int(coordinates[0]), int(coordinates[1])) == True:
				system('clear')
				print_board(board)
				return p_two
			turn += 1
	return None


def huvsai(ts):
	board = init_board()
	player_one = 'O'
	player_ai = 'X'
	for turn in range(ts, 9+ts):
		if turn % 2 != 0:
			sleep(1)
			board, ai_coordinates = get_ai_move(board, player_ai)
			if has_won(board, int(ai_coordinates[0]), int(ai_coordinates[1])) == True:
				system('clear')
				print_board(board)
				return player_ai
			turn += 1
		else:
			sleep(1)
			board, coordinates = _turn_(board, player_one)
			if has_won(board, int(coordinates[0]), int(coordinates[1])) == True:
				system('clear')
				print_board(board)
				return player_one
			turn += 1
	return None


def aivsai():
	board = init_board()
	ai_one = 'O'
	ai_two = 'X'
	for turn in range(9):
		if turn % 2 != 0:
			sleep(1)
			board, ai_coordinates = get_ai_move(board, ai_one)
			system('clear')
			print_board(board)
			if has_won(board, int(ai_coordinates[0]), int(ai_coordinates[1])) == True:
				system('clear')
				print_board(board)
				return ai_one
			turn += 1
		else:
			board, ai_coordinates = get_ai_move(board, ai_two)
			sleep(1)
			system('clear')
			print_board(board)
			if has_won(board, int(ai_coordinates[0]), int(ai_coordinates[1])) == True:
				system('clear')
				print_board(board)
				return ai_two
			turn += 1
	return None


def tictactoe_game(mode='HUMAN-HUMAN'):
	if mode == 1:
		while True:
			system('clear')
			winner = huvshu('Player O', 'Player X')
			if winner == None:
				input('\n\tIt\'s a tie!')
				system('clear')
				main_menu()
			else:
				input(f'\n\t{winner} WIN!')
				system('clear')
				main_menu()
	elif mode == 2 or mode == 3:
		while True:
			system('clear')
			if mode == 2:
				ts = 0
			else:
				ts = 1	
			winner = huvsai(ts)
			if winner == None:
				input('\n\tIt\'s a tie!')
				system('clear')
				main_menu()
			else:
				input(f'\n\t{winner} WIN!')
				system('clear')
				main_menu()
	elif mode == 4:
		while True:
			system('clear')
			winner = aivsai('AI ONE', 'AI TWO')
			if winner == None:
				input('\n\tIt\'s a tie!')
				system('clear')
				main_menu()
			else:
				input(f'\n\t{winner} WIN!')
				system('clear')
				main_menu()


def main_menu():
	main_title()
	print('\n\n\n')
	print("1. Human  vs.  Human".center(120))
	print('\n')
	print("2. Human  vs.  AI".center(120))
	print('\n')
	print("3. AI vs. Human".center(120))
	print('\n')
	print("4. AI vs. AI".center(120))
	print('\n')
	print("Choose game mode or enter 'quit':".center(120))
	print()

	mode = input(''.center(60)).lower()
	if mode == 'quit':
		exit()
	elif mode == 1 or 2 or 3:
		tictactoe_game(int(mode))


if __name__ == '__main__':
    main_menu()