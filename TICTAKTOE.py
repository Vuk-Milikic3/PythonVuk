import random

def print_board(board):
    """Druckt das aktuelle Spielfeld."""
    for row in [board[i:i+3] for i in range(0, len(board), 3)]:
        print(" | ".join(row))
        if board.index(row[0]) < 6:
            print("--+---+--")

def check_win(board, player):
    """Überprüft, ob der angegebene Spieler gewonnen hat."""
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontale Gewinnmöglichkeiten
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertikale Gewinnmöglichkeiten
                      (0, 4, 8), (2, 4, 6)]            # Diagonale Gewinnmöglichkeiten
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_tie(board):
    """Überprüft, ob es ein Unentschieden gibt."""
    return all([spot in ['x', 'o'] for spot in board])

def player_move(board, player):
    """Lässt den Spieler einen Zug machen."""
    move = int(input("Wähle dein Feld aus (1-9): ")) - 1
    if board[move] not in ['x', 'o']:
        board[move] = player
    else:
        print("Feld bereits belegt. Versuche es erneut.")
        player_move(board, player)

def ai_move(board):
    """KI macht einen zufälligen Zug."""
    available_moves = [i for i in range(9) if board[i] not in ['x', 'o']]
    move = random.choice(available_moves)
    board[move] = 'o'

def tic_tac_toe():
    """Hauptfunktion für das Tic-Tac-Toe-Spiel."""
    board = [str(i+1) for i in range(9)]
    current_player = 'x'
    game_over = False
    
    while not game_over:
        print_board(board)
        if current_player == 'x':
            player_move(board, current_player)
        else:
            ai_move(board)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Spieler {current_player} hat das Spiel gewonnen.")
            game_over = True
        elif check_tie(board):
            print_board(board)
            print("Unentschieden!")
            game_over = True
        else:
            current_player = 'o' if current_player == 'x' else 'x'
    
    restart = input("Möchtest du ein weiteres Spiel spielen? (y/n): ")
    if restart.lower() == 'y':
        tic_tac_toe()

# Spiel starten
tic_tac_toe()
