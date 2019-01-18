import os
import random

#Function to Check If user input is correct
def check_input(inputvariable,data_list):
    while True:
        if inputvariable in data_list:
            break
        print("Wrong Input! Please enter Again")
        inputvariable=input()
    return inputvariable

#Function to Check If user input is in range or not
def check_input_int(inputvariable,data_list):
    while True:
        if int(inputvariable) in data_list:
            break
        print("Wrong Input! Please enter Again")
        inputvariable=input()
    return inputvariable

#Function to randomly choose which player plays first turn
def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

#Function to Check if board is empty at specified position
def space_check(board, position):
    return board[position-1] == ' '

#Function to Check If Board Is Full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#Function to clear the board
def clear():
    os.system( 'cls' )

#Function to display the board
def display_board(board):
    print(" {0} | {1} | {2}".format(board[0],board[1],board[2]))
    print("-"*11)
    print(" {0} | {1} | {2}".format(board[3],board[4],board[5]))
    print("-"*11)
    print(" {0} | {1} | {2}".format(board[6],board[7],board[8]))

#Function to place the marker
def place_marker(board,symbol,position):
    clear()
    board[position-1]=symbol

#Function to Check if the user has won the game
def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[6] == mark and board[7] == mark and board[8] == mark) or # across the bottom
    (board[0] == mark and board[4] == mark and board[8] == mark) or # down the middle
    (board[2] == mark and board[4] == mark and board[6] == mark) or # down the middle
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down the last line
    (board[0] == mark and board[3] == mark and board[6] == mark) or # down the first line
    (board[1] == mark and board[4] == mark and board[7] == mark)) # down the middle

#Function To mark at player choice
def player_choice(board):
    position = -1
    position = int(input('Choose your next position: (1-9) '))
    position=check_input_int(position,range(1,10))
    while  not space_check(board, position):
        print("That Position is already filled")
        position = int(input('Choose your next position: (1-9) '))
    check_input_int(position,range(1,10))
    return position

#Function to ask if user wanna play the game again
def replay():
    print("Wanna Play Again (Y/N) : ")
    play_again=input()
    play_again=check_input(play_again,['Y','y','N','n'])
    if play_again in ['Y','y']:
        play_again=True
    elif play_again in ['N','n']:
        play_again=False
    return play_again

#Printing the welcome message
print("*"*29)
print('|  Welcome to Tic Tac Toe!  |')
print("*"*29)


while True:
    
    # input for first Symbol
    print("Enter User 1 Symbol (X or O)")
    symbol1=input()
    symbol1=check_input(symbol1,['x', 'X', 'o','O'])

    # input for second Symbol
    print("Enter User 2 Symbol (X or O)")
    symbol2=input()
    symbol2=check_input(symbol2,['x', 'X', 'o','O'])

    Board = [' '] * 9                              #Creating the tic-tac-toe board

    turn = choose_first()
    print(turn + ' will go first.')
    game_on=True

    while game_on:

        #Player 1 Turn
        if turn == 'Player 1':
            display_board(Board)                   #Displaying the board
            print("\nPlayer 1 Chance ")
            position = player_choice(Board)        #Asking for the position to mark
            place_marker(Board, symbol1, position) #Placing the symbol at the position user typed

            if win_check(Board, symbol1):
                display_board(Board)
                print('Congratulations! Player 1 won the game!')
                break                              #Breaking the loop as the game is over
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        
        else :

            #Player 2 turn
            display_board(Board)
            
            print("\nPlayer 2 Chance ")
            position_1=player_choice(Board)
            place_marker(Board,symbol2,position_1)

            if win_check(Board,symbol2):
                display_board(Board)
                print("Congratulations! Player 2 won the game !")
                break
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
        
    if not replay():                               #Checking If user want to play the game again
        break                                   



