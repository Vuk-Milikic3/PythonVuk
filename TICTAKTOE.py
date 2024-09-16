import random

print("Welcome to Tic Tac Toe")
print("----------------------")

player1_symbol = 'X'
player2_symbol = 'O'

def create_new_board():
    return [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

def game_board(board):
    print("+---+---+---+")
    for row in board:
        print(f"| {' | '.join(str(cell) for cell in row)} |")
        print("+---+---+---+")

def get_player_move(player_symbol):
    while True:
        try:
            move = int(input(f"Player {player_symbol}, choose a field (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def update_board(board, move, player_symbol):
    field_coordinates = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    row, col = field_coordinates[move]
    if board[row][col] not in [player1_symbol, player2_symbol]:
        board[row][col] = player_symbol
        return True
    else:
        print("This field is already taken. Please choose another field.")
        return False

def check_for_winner(board):

    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None

def ask_to_play_again():
    while True:
        answer = input("Do you want to play another game? (yes/no): ").lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please answer with 'yes' or 'no'.")

def select_game_mode():
    while True:
        mode = input("Do you want to play against the computer or another player? (computer/player): ").lower()
        if mode in ["player", "p"]:
            return "player"
        elif mode in ["computer", "c"]:
            print("Computer opponent is not implemented yet.")
            return None
        else:
            print("Please answer with 'computer' or 'player'.")

def play_game():
    board = create_new_board()
    game_mode = select_game_mode()
    if game_mode != "player":
        return



    current_player_symbol = player1_symbol

    for total_moves in range(9):
        game_board(board)
        
        # Get player move
        move = get_player_move(current_player_symbol)
        
        if not update_board(board, move, current_player_symbol):
            continue
        
        winner = check_for_winner(board)
        if winner:
            game_board(board)
            print(f"{winner} wins!")
            return
        
        current_player_symbol = player2_symbol if current_player_symbol == player1_symbol else player1_symbol
        

    game_board(board)
    print("It's a tie!")


while True:
    play_game()
    if not ask_to_play_again():
        print("Thanks for playing! Goodbye!")
        break