import random

print("Welcome to Tic Tac Toe")
print("----------------------")

# Initialisiere das Spielfeld mit Zahlen von 1 bis 9
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def printGameBoard():
    # Zeigt das Spielfeld an
    for row in gameBoard:
        print("+---+---+---+")
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print("+---+---+---+")

def modifyArray(number, player):
    # Bestimmt die Zeile und Spalte basierend auf der eingegebenen Zahl
    row = (number - 1) // 3
    col = (number - 1) % 3

    # Setzt den Zug des Spielers, wenn der Platz noch frei ist
    if gameBoard[row][col] not in ["X", "O"]:
        gameBoard[row][col] = player
    else:
        print("This spot is already taken. Try again.")

def checkWinner():
    # Überprüft jede Zeile auf einen Gewinner
    for row in gameBoard:
        if row[0] == row[1] == row[2]: 
            return row[0]

    # Überprüft jede Spalte auf einen Gewinner
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col]:
            return gameBoard[0][col]

    # Überprüft die erste Diagonale auf einen Gewinner
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]

    # Überprüft die zweite Diagonale auf einen Gewinner
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]

    # Gibt None zurück, wenn es keinen Gewinner gibt
    return None

def playGame():
    # Definiert den aktuellen Spieler und die Anzahl der Züge
    currentPlayer = "X"
    moves = 0

    # Das Spiel läuft bis maximal 9 Züge gemacht wurden
    while moves < 9:
        printGameBoard()

        # Frage den aktuellen Spieler nach einem Zug
        try:
            move = int(input(f"Player {currentPlayer}, choose a number (1-9): "))
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        # Überprüfe, ob die eingegebene Zahl im gültigen Bereich liegt
        if move < 1 or move > 9:
            print("Invalid move. Please try again.")
            continue

        # Setze den Zug für den aktuellen Spieler
        modifyArray(move, currentPlayer)

        # Überprüfe, ob es einen Gewinner gibt
        winner = checkWinner()
        if winner:
            printGameBoard()
            print(f"Player {winner} wins!")
            return

        # Wechsle den aktuellen Spieler
        currentPlayer = "O" if currentPlayer == "X" else "X"

        # Erhöhe die Anzahl der Züge
        moves += 1

    # Wenn alle 9 Züge gemacht wurden und es keinen Gewinner gibt, ist es ein Unentschieden
    printGameBoard()
    print("It's a tie!")

# Starte das Spiel
playGame()
