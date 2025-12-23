from copy import deepcopy
from .board import ROWS, COLS, EMPTY, PLAYER_MAX, PLAYER_MIN


def is_valid_move(board, col):
    if col < 0:
        return False
    if col >= COLS:
        return False
    if board[0][col] == EMPTY:
        return True
    else:
        return False



def get_valid_moves(board):
    valid_moves = []
    for c in range(COLS):
        if is_valid_move(board, c):
            valid_moves.append(c)
    return valid_moves



def make_move(board, col, player):
    new_board = deepcopy(board)
    for row in range(ROWS - 1, -1, -1):
        if new_board[row][col] == EMPTY:
            new_board[row][col] = player
            break
    return new_board


def check_winner(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for r in range(ROWS):
        for c in range(COLS):
            player = board[r][c]
            if player == EMPTY:
                continue
            for dr, dc in directions:
                count = 0
                rr, cc = r, c
                for _ in range(4):
                    if 0 <= rr < ROWS and 0 <= cc < COLS and board[rr][cc] == player:
                        count += 1
                        rr += dr
                        cc += dc
                    else:
                        break
                if count == 4:
                    return player
    return None


def is_full(board):
   
    for c in range(COLS):
        if board[0][c] == EMPTY:
           
            return False
    return True


def is_terminal(board):
    winner = check_winner(board)
    if winner is not None:
        return True
    if is_full(board):
        return True
    return False
