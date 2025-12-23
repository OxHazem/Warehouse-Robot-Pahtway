from Phase2_game.game.board import ROWS, COLS, EMPTY, PLAYER_MAX, PLAYER_MIN


def score_window(window, player):
    if player == PLAYER_MAX:
        opp = PLAYER_MIN
    else:
        opp = PLAYER_MAX
    score = 0
    player_count = window.count(player)
    opp_count = window.count(opp)
    empty_count = window.count(EMPTY)
    if player_count == 4:
        score = score + 1000
    elif player_count == 3 and empty_count == 1:
        score = score + 10
    elif player_count == 2 and empty_count == 2:
        score = score + 5
    if opp_count == 3 and empty_count == 1:
        score = score - 8

    return score


def evaluate_board(board, player):
    score = 0
    center_index = COLS // 2
    center_count = 0
    for r in range(ROWS):
        if board[r][center_index] == player:
            center_count = center_count + 1
    score = score + (center_count * 3)
    for r in range(ROWS):
        for c in range(COLS - 3):
            window = [
                board[r][c],
                board[r][c + 1],
                board[r][c + 2],
                board[r][c + 3]
            ]
            score = score + score_window(window, player)
    for c in range(COLS):
        for r in range(ROWS - 3):
            window = [
                board[r][c],
                board[r + 1][c],
                board[r + 2][c],
                board[r + 3][c]
            ]
            score = score + score_window(window, player)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [
                board[r][c],
                board[r + 1][c + 1],
                board[r + 2][c + 2],
                board[r + 3][c + 3]
            ]
            score = score + score_window(window, player)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [
                board[r][c],
                board[r - 1][c + 1],
                board[r - 2][c + 2],
                board[r - 3][c + 3]
            ]
            score = score + score_window(window, player)
    return score

