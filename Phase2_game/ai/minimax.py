import math
import random
from Phase2_game.game.logic import *
from Phase2_game.ai.evaluation import evaluate_board


def minimax(board, depth, maximizing_player, node_counter):
    node_counter["count"] += 1

    winner = check_winner(board)
    if depth == 0 or is_terminal(board):
        if winner == PLAYER_MAX:
            return 10000, None
        elif winner == PLAYER_MIN:
            return -10000, None
        return evaluate_board(board, PLAYER_MAX), None

    valid_moves = get_valid_moves(board)
    if maximizing_player:
        value = -math.inf
        best = None
        for col in valid_moves:
            child = make_move(board, col, PLAYER_MAX)
            new_score, _ = minimax(child, depth - 1, False, node_counter)
            if new_score > value:
                value = new_score
                best = col
        return value, best

    else:
        value = math.inf
        best = None
        for col in valid_moves:
            child = make_move(board, col, PLAYER_MIN)
            new_score, _ = minimax(child, depth - 1, True, node_counter)
            if new_score < value:
                value = new_score
                best = col
        return value, best
