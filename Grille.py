board= ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
print("", board[0], "|", "", board[1], "|", "", board[2])
print("---|----|---")
print("", board[3], "|", "", board[4], "|", "", board[5])
print("---|----|---")
print("", board[6], "|", "", board[7], "|", "", board[8])

def condition():
    if board[0] == board[1] == board[2]:
        elif board[0] == board[3] == board[6]:
        elif board[0] == board[4] == board[8]:
        elif board[1] == board[4] == board[7]:
        elif board[2] == board[4] == board[6]:
        elif board[2] == board[5] == board[8]:
        elif board[3] == board[4] == board[5]:
        elif board[6] == board[7] == board[8]:
        else print("Match nul"):