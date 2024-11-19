

import random

# Initialize the game board
board = [" " for _ in range(9)]

# Function to show the game board
def show_board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---|---|---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---|---|---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# Function to check for a win
def check_win():
    if board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    else:
        return False

# Function to ask the player for a move
def get_move():
    while True:
        try:
            move = int(input("Choose a cell from 1 to 9: "))
            if 1 <= move <= 9:
                return move - 1
            print('Please choose a valid cell!')
        except ValueError:
            print('You need to choose a number from 1 to 9.')

# Function to check for a draw
def check_draw():
    return " " not in board

# Function for the AI to make a move
def ia(board, symbol):
    opponent = "O" if symbol == "X" else "X"

    #Check if the AI can win
    for i in range(9):
        if board[i] == " ":
            board[i] = symbol
            if check_win():
                board[i] = " "
                return i
            board[i] = " "

    #Check if the AI needs to block the opponent
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if check_win():
                board[i] = " "
                return i
            board[i] = " "

    #Play in the center if possible
    if board[4] == " ":
        return 4

    #  Play in a corner if possible
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            return i

    #Play in any available cell
    for i in range(9):
        if board[i] == " ":
            return i

    return False

# Main function to play the game
def play():
    player_1 = input("What is your name? ")
    play_against_ai = input("Do you want to play against the computer? (yes/no): ").strip().lower()

    if play_against_ai == "yes":
        player_2 = "Computer"
        players = [(player_1, "X"), (player_2, "O")]
    else:
        player_2 = input("What is your name? ")
        players = [(player_1, "X"), (player_2, "O")]

    current_player = random.choice(players)
    print(f"{current_player[0]}, you start with {current_player[1]}")

    while True:
        show_board()
        print(f"It's {current_player[0]}'s turn")
        
        if current_player[0] == "Computer":
            move = ia(board, current_player[1])
            print(f"The computer chose cell {move + 1}")
        else:
            move = get_move()
        
        if board[move] != " ":
            print("This cell is already taken!")
            continue
        
        board[move] = current_player[1]
        
        if check_win():
            show_board()
            print(f"Congratulations! {current_player[0]} won!")
            break
        elif check_draw():
            show_board()
            print("It's a draw!")
            break
            
        current_player = players[0] if current_player == players[1] else players[1]

play()
