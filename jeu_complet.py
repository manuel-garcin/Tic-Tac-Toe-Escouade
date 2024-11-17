import random

# Initialize the game board
board = [" " for _ in range(9)]

# Function to display the game board
def display_board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---|---|---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---|---|---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# Function to check for a win condition
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

# Function to ask the player to choose a cell
def ask_for_move():
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

# Main function to play the game
def play_game():
    player_1 = input('What is your name? ')
    player_2 = input('What is your name? ')
    players = [(player_1, "X"), (player_2, "O")]
    current_player = random.choice(players)
    print(f"{current_player[0]}, you start with {current_player[1]}")
    
    while True:
        display_board()
        print(f"It's {current_player[0]}'s turn")
        move = ask_for_move()
        if board[move] != " ":
            print("This cell is already taken!")
            continue
        board[move] = current_player[1]
        
        if check_win():
            display_board()
            print(f"Congratulations! {current_player[0]}, you won!")
            break
        elif check_draw():
            display_board()
            print("It's a draw!")
            break
            
        current_player = players[0] if current_player == players[1] else players[1]

play_game()
