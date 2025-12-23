ROWS = 6
COLS = 7

EMPTY = 0
PLAYER_MAX = 1  
PLAYER_MIN = -1  


def create_board():
    board = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append(EMPTY)
        board.append(row)
    return board


def print_board(board):
    for row in board:
        line = ""
        for cell in row:
            if cell == EMPTY:
                line += ". "
            elif cell == PLAYER_MAX:
                line += "X "
            elif cell == PLAYER_MIN:
                line += "O "
        print(line.strip())
    print("0 1 2 3 4 5 6")
    print()

    