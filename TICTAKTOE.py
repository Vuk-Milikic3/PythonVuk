import random

print("Welcome to Tic Tac Toe")
print("----------------------")

def resetGameBoard():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

gameBoard = resetGameBoard()

def printGameBoard():

    print("+---+---+---+")
    print(f"| {gameBoard[0][0]} | {gameBoard[0][1]} | {gameBoard[0][2]} |")
    print("+---+---+---+")
    print(f"| {gameBoard[1][0]} | {gameBoard[1][1]} | {gameBoard[1][2]} |")
    print("+---+---+---+")
    print(f"| {gameBoard[2][0]} | {gameBoard[2][1]} | {gameBoard[2][2]} |")
    print("+---+---+---+")

def modifyArray(number, player):

    if number == 1:
        if gameBoard[0][0] != "X" and gameBoard[0][0] != "O":
            gameBoard[0][0] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 2:
        if gameBoard[0][1] != "X" and gameBoard[0][1] != "O":
            gameBoard[0][1] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 3:
        if gameBoard[0][2] != "X" and gameBoard[0][2] != "O":
            gameBoard[0][2] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 4:
        if gameBoard[1][0] != "X" and gameBoard[1][0] != "O":
            gameBoard[1][0] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 5:
        if gameBoard[1][1] != "X" and gameBoard[1][1] != "O":
            gameBoard[1][1] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 6:
        if gameBoard[1][2] != "X" and gameBoard[1][2] != "O":
            gameBoard[1][2] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 7:
        if gameBoard[2][0] != "X" and gameBoard[2][0] != "O":
            gameBoard[2][0] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 8:
        if gameBoard[2][1] != "X" and gameBoard[2][1] != "O":
            gameBoard[2][1] = player
        else:
            print("This spot is already taken. Try again.")
    elif number == 9:
        if gameBoard[2][2] != "X" and gameBoard[2][2] != "O":
            gameBoard[2][2] = player
        else:
            print("This spot is already taken. Try again.")
    else:
        print("Invalid input, please enter a number between 1 and 9.")

def checkWinner():

    if gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2]:
        return gameBoard[0][0]
    elif gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2]:
        return gameBoard[1][0]
    elif gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2]:
        return gameBoard[2][0]
    
    if gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0]:
        return gameBoard[0][0]
    elif gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1]:
        return gameBoard[0][1]
    elif gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2]:
        return gameBoard[0][2]

    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]
    elif gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]

    return None

def playGame():

    currentPlayer = "X"
    moves = 0

    while moves < 9:
        printGameBoard()

        try:
            move = int(input(f"Player {currentPlayer}, choose a number (1-9): "))
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        if move < 1 or move > 9:
            print("Invalid move. Please try again.")
            continue

        modifyArray(move, currentPlayer)

        winner = checkWinner()
        if winner:
            printGameBoard()
            print(f"Player {winner} wins!")
            return

        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"

        moves += 1

    printGameBoard()
    print("It's a tie!")

def askForAnotherGame():
    while True:
        answer = input("Do you want to play another game? (yes/no): ").lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Please answer with 'yes' or 'no'.")

while True:
    playGame()
    if not askForAnotherGame():
        print("Thanks for playing! Goodbye!")
        break
    else:
        gameBoard = resetGameBoard()
