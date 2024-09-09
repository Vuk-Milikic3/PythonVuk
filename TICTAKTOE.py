import random

print("Welcome to Tic Tac Toe")
print("----------------------")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+")

def modifyArray(number, turn):
    number -= 1  
    if number == 0:
        gameBoard[0][0] = turn
    elif number == 1:
        gameBoard[0][1] = turn
    elif number == 2:
        gameBoard[0][2] = turn
    elif number == 3:
        gameBoard[1][0] = turn
    elif number == 4:
        gameBoard[1][1] = turn
    elif number == 5:
        gameBoard[1][2] = turn
    elif number == 6:
        gameBoard[2][0] = turn
    elif number == 7:
        gameBoard[2][1] = turn
    elif number == 8:
        gameBoard[2][2] = turn

leaveLoop = False
turnCounter = 0

