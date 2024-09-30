import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

canvas_size = 300
line_thickness = 5
current_player = 'X'
game_mode = None

title_label = tk.Label(root, text="TICTACTOE", font=('Arial', 24, 'bold'), fg="black")
title_label.pack(pady=10)

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white", highlightthickness=0)
canvas.pack(pady=20)

buttons = [[None for _ in range(3)] for _ in range(3)]

def select_game_mode():
    global game_mode
    game_mode = messagebox.askquestion("Select Mode", "Do you want to play against the computer? (yes for computer, no for player)")
    reset_board()

def check_for_winner():
    board = [[buttons[row][col]["text"] for col in range(3)] for row in range(3)]
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

def check_tie():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def handle_click(row, col):
    global current_player
    button = buttons[row][col]
    if button["text"] == "":
        button.config(text=current_player)
        winner = check_for_winner()
        if winner:
            display_winner(f"{winner} wins!")
        elif check_tie():
            display_winner("It's a tie!")
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            if game_mode == 'yes' and current_player == 'O':
                root.after(500, computer_move)  

def display_winner(message):
    for row in buttons:
        for button in row:
            button.config(state="disabled")
    title_label.config(text=message)

def reset_board():
    global current_player
    current_player = 'X'
    title_label.config(text="TICTACTOE")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state="normal")
            buttons[row][col].place(x=col * button_size, y=row * button_size, width=button_size, height=button_size)

def get_available_moves():
    available_moves = []
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                available_moves.append((row, col))
    return available_moves

def computer_move():
    global current_player
    available_moves = get_available_moves()

    for row, col in available_moves:
        buttons[row][col].config(text="O")
        if check_for_winner() == "O":
            winner = check_for_winner()
            if winner:
                display_winner(f"{winner} wins!")
            return
        buttons[row][col].config(text="")

    for row, col in available_moves:
        buttons[row][col].config(text="X")
        if check_for_winner() == "X":
            buttons[row][col].config(text="O")
            break
        buttons[row][col].config(text="")
    else:
        if (1, 1) in available_moves:
            buttons[1][1].config(text="O")
        else:
            move = random.choice(available_moves)
            buttons[move[0]][move[1]].config(text="O")

    winner = check_for_winner()
    if winner:
        display_winner(f"{winner} wins!")
    elif check_tie():
        display_winner("It's a tie!")
    else:
        current_player = 'X'

button_size = canvas_size // 3
for row in range(3):
    for col in range(3):
        button = tk.Button(canvas, text="", font=('Arial', 20), width=5, height=2,
                           command=lambda r=row, c=col: handle_click(r, c))
        button.place(x=col * button_size, y=row * button_size, width=button_size, height=button_size)
        buttons[row][col] = button

restart_button = tk.Button(root, text="Restart", width=25, height=3, font=('Arial', 12, 'bold'), command=reset_board)
restart_button.pack(pady=20)

select_game_mode()

root.mainloop()
