# Function for the AI to make a move
def ia(board, symbol):
    opponent = "O" if symbol == "X" else "X"

    # 1. Check if the AI can win
    for i in range(9):
        if board[i] == " ":
            board[i] = symbol
            if check_win():
                board[i] = " "
                return i
            board[i] = " "

    # 2. Check if the AI needs to block the opponent
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if check_win():
                board[i] = " "
                return i
            board[i] = " "

    # 3. Play in the center if possible
    if board[4] == " ":
        return 4

    # 4. Play in a corner if possible
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            return i

    # 5. Play in any available cell
    for i in range(9):
        if board[i] == " ":
            return i

    return False