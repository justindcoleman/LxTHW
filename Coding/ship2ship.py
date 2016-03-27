from random import randint
#globals 
#
#list containing the play area
board = []
#used to track turns taken
turn = 0
#end globals

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row,",", ship_col