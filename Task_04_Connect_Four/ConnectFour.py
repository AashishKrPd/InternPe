# Importing all the required Modules
from random import randint, choice
from time import sleep
from os import listdir, getcwd

# Default Rows and Columns
cols = 7
rows = 6

# Welcome Screen to Greeting User 
print("\n\t"+f"Welcome to Game Connect 4".center(5*cols+1, ' '))
print("\t"+str("-"*(25)).center(5*cols+1, ' ')) # Line


a = ord('A') # refference variable
letters = [chr(a+i) for i in range(cols)] # Columns letter
gameBoard = [["" for _ in range(cols)] for _ in range(rows)] # game Board as 2D matrix


def printGameBoard():
    '''Print Board of Connect Four Game'''
    
    def printLetters(extra = ""):
        '''Print Alphabets only'''
        print(end=f"{extra}\t")
        for i in letters:
            print(f"   {i} ",end="")
        print()
        
    def printBoxs():
        '''Draw all Box and its values in CUI'''  
        print() 
        for x in range(rows):
            print("\t+"+"----+"*cols)
            # print(f"     {x}  |", end="")
            print("        |", end="")
            for y in range(cols):
                if (gameBoard[x][y] == "🔵"):
                    print(f" {gameBoard[x][y]} ", end="|")
                elif (gameBoard[x][y] == "🔴"):
                    print(f" {gameBoard[x][y]} ", end="|")
                else:
                    print(f"  {gameBoard[x][y]}  ", end="|")
            # print(f"{i}"+"\t|"*(cols+1) , end="")
            print()
        print("\t+"+"----+"*cols)
    
    # Calling Box and Letter function 
    printBoxs()
    printLetters()


def modifyArray(spacedPick, turn):
    '''Updating value of GameBoard'''
    gameBoard[spacedPick[0]] [spacedPick[1]] = turn
    
    
def chechForWinner(chip):
    '''Checking all the winning conditions of game'''
    
    # check Horizontal
    for y in range(rows):
        for x in range(cols - 3):
            if (gameBoard[y][x] == chip and gameBoard[y][x+1] == chip and gameBoard[y][x+2] == chip and gameBoard[y][x+3] == chip):
                return True
            
    # check Vertical
    for y in range(rows-3):
        for x in range(cols):
            if (gameBoard[y][x] == chip and gameBoard[y+1][x] == chip and gameBoard[y+2][x] == chip and gameBoard[y+3][x] == chip):
                return True
    
    # check Diagonal (top right to  bottom left)
    for x in range(rows - 3):
        for y in range(3, cols):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip):
                return True
    
    # check Diagonal (top left to bottom right)
    for x in range(rows - 3):
        for y in range(cols - 3):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip):
                return True
            
    return False 


def isSpaceAvailable(cord):
    '''check if a particular Coordinate is Empty or Not'''
    if (gameBoard[cord[0]][cord[1]] == '🔴'):
        return False
    elif (gameBoard[cord[0]][cord[1]] == '🔵'):
        return False
    else:
        return True


def coordinatePhaserWithGravity(InStr):
    '''Take "A" and convert it into [row, col] as per gravity applied'''
    
    cord = [None]*2
    ref = ord('A') # Refference Variable
    
    # checking if Alphabet is given and also should be in range of column numbers 
    if 'A'<=InStr[0].upper()<='Z' and InStr[0].upper()<chr(ref+cols):
        cord[1] = ord(InStr[0].upper())-ref
    else:
        print("Invalid!")
    
    # Applying gravity to find bottom most coordinate 
    for i in range(rows-1, -1, -1):
        if isSpaceAvailable([i, cord[1]]):
            cord[0] = i
            break
        
    return cord


def allFilled():
    '''Testing all place is filled or not for Draw Case'''
    for r in gameBoard:
        if "" in r:
            return False
    return True
        
        
# definging important Variables 
turnCounter = 0
winner = None

# Progame Flow Starts From Here
while True:
    printGameBoard() # Printing Game Board on Each Itteration
    
    if winner: # if we got a winner printing Winner and Updating Level of Game for next Round
        if turnCounter % 2 == 0:
            print("\n\t"+f"Game Over! 🔴 'Bot Won!'".center(5*cols+1, ' '))
            print("\t"+"Beat Me! 🤖".center(5*cols+1, ' ')+"\n")
        else:
            print("\n\t"+f"Game Over! 🔵 'You Won!'".center(5*cols+1, ' '))
            print("\t"+"Thanks for Playing 😃".center(5*cols+1, ' ')+"\n")
        break
    
    if allFilled(): # If all filled Printing Draw | No one Won
        print("\n\t"+f"Game Over! It's Draw!".center(5*cols+1, ' '))
        print("\t"+"Please Play Again! 😕".center(5*cols+1, ' ')+"\n")
        break
    
    if turnCounter % 2 == 0: # If User got a Change
        while True:
            spacePicked = input("\nEnter an Alphabet: ")
            try:
                # Parsing Coordiantes and Checking for available Space
                coordinate = coordinatePhaserWithGravity(spacePicked)
                if isSpaceAvailable(coordinate):
                    modifyArray(coordinate, '🔵') # updating
                    break
                else:
                    print("not a valid coordinate")
            except:
                print("Error occupied! Play try again.")
        
        winner = chechForWinner('🔵') # Assign user winner
        
    else:
        while True:
            let = choice(letters) # let Bot Randomly choose a letter in the given Range
            cpuChoice = [let, randint(0, rows-1)]
            
            print(f"\nEnter by Bot: {let}")
            try:
                cpuCord = coordinatePhaserWithGravity(cpuChoice)
            
                if isSpaceAvailable(cpuCord):
                    sleep(0.5) # slowing it down to make it feels more human
                    modifyArray(cpuCord, '🔴') # Updating
                    break
            except:
                pass # If bot enter already filled column 
            
        winner = chechForWinner('🔴') # Got Bot as winner
        
    turnCounter += 1  # Updating turn two get equal chances 

input()