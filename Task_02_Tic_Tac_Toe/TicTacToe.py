# Importing Required Modules 
from random import randint
from time import sleep

# Global Variables 
# Tic Tac Toe Board as list 
board = [" ",]*9

# Defining Player and Bot Letters
player = "X"
bot = "O"


def printBoard(board):
    '''Takes a dictonary boardThis Function Print Tic Tac Tao Board'''
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    

def isFree(pos):
    '''This take postion and check if that index element is " " or not'''
    if board[pos-1] == " ":
        return True
    else:
        return False

def checkDraw():
    '''Check if the Match Draw between User and BOT'''
    if " " not in board:
        return True
    else:
        return False

def checkForWin():
    '''Check all the Possible Direction to check Game is Won or Not'''
    if (board[0] == board[1] == board[2] and board[0] != ' '):
        return True
    elif (board[3] == board[4] == board[5] and board[3] != ' '):
        return True
    elif (board[6] == board[7] == board[8] and board[6] != ' '):
        return True
    elif (board[0] == board[3] == board[6] and board[0] != ' '):
        return True
    elif (board[1] == board[4] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] == board[8] and board[2] != ' '):
        return True
    elif (board[0] == board[4] == board[8] and board[0] != ' '):
        return True
    elif (board[6] == board[4] == board[2] and board[6] != ' '):
        return True
    else:
        return False

def insertLetter(letter, position):
    '''Takes a Letter and Insert that letter at Position given in Board'''
    if isFree(position):
        board[position-1] = letter
        printBoard(board)
        if checkForWin():
            print()
            if letter == 'O':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        if (checkDraw()):
            print("Draw!")
            exit()
        

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        


def playerMove():
    '''User Turn to place X on Board as per Given Position'''
    position = int(input("Enter the position for 'X':  "))
    insertLetter(player, position)


def compMove():
    '''Bot Turn to place O on Board by Generating random Number'''
    while " " in board:
        position = randint(1, 9) 
        if isFree(position):
            print(f"Position By Bot for 'O':  {position}")
            insertLetter(bot, position)
            break



# Printing Borad in the Starting of the Game 
printBoard(board)

# Game Run until Anyone Win or Game get Draw 
while not checkForWin():
    print()
    playerMove()
    sleep(1) # Sleep for 1 sec to make bot behave like it is thinking...
    print()
    compMove()
    