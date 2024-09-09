import random

print("Welcome to Tic Tac Toe")
print("----------------------")


gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def printGameBoard():

    for row in gameBoard:
        print("+---+---+---+")
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print("+---+---+---+")

def modifyArray(number, player):

    row = (number - 1) // 3
    col = (number - 1) % 3

    if gameBoard[row][col] not in ["X", "O"]:
        gameBoard[row][col] = player
    else:
        print("This spot is already taken. Try again.")


def checkWinner():
    
    for row in gameBoard:
        if row[0] == row[1] == row[2]: 
            return row[0]

    
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col]:
            return gameBoard[0][col]

    
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]

   
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]

    
    return None