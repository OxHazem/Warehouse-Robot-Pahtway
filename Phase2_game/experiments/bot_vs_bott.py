from Phase2_game.game.board import create_board, print_board, PLAYER_MAX, PLAYER_MIN
from Phase2_game.game.logic import make_move, is_terminal, check_winner
from Phase2_game.ai.minimax import minimax
from Phase2_game.ai.alphabeta import alphabeta
from Phase2_game.ai.random_bot import random_bot
import math
import time


def play_match(ai1, ai2, depth=4, verbose=False):
    """
    ai1 = function for player MAX
    ai2 = function for player MIN
    """
    board = create_board()
    current = PLAYER_MAX

    moves = 0

    while True:
        if is_terminal(board):
            winner = check_winner(board)
            return winner, moves

        if current == PLAYER_MAX:
            move = ai1(board, depth)
            board = make_move(board, move, PLAYER_MAX)
            current = PLAYER_MIN
        else:
            move = ai2(board, depth)
            board = make_move(board, move, PLAYER_MIN)
            current = PLAYER_MAX

        moves += 1
        if verbose:
            print_board(board)




def minimax_ai(board, depth):
    node_counter = {"count": 0}
    score, move = minimax(board, depth, True, node_counter)
    return move


def alphabeta_ai(board, depth):
    node_counter = {"count": 0}
    score, move = alphabeta(board, depth, -math.inf, math.inf, True, node_counter)
    return move


def random_ai(board, depth=None):
    return random_bot(board)




def run_experiments(games=10, depth=4):
    results = {
        "minimax_vs_random": {"minimax": 0, "random": 0, "draw": 0},
        "alphabeta_vs_random": {"alphabeta": 0, "random": 0, "draw": 0}
    }

    
    for _ in range(games):
        winner, _ = play_match(minimax_ai, random_ai, depth)
        if winner == PLAYER_MAX:
            results["minimax_vs_random"]["minimax"] += 1
        elif winner == PLAYER_MIN:
            results["minimax_vs_random"]["random"] += 1
        else:
            results["minimax_vs_random"]["draw"] += 1

   
    for _ in range(games):
        winner, _ = play_match(alphabeta_ai, random_ai, depth)
        if winner == PLAYER_MAX:
            results["alphabeta_vs_random"]["alphabeta"] += 1
        elif winner == PLAYER_MIN:
            results["alphabeta_vs_random"]["random"] += 1
        else:
            results["alphabeta_vs_random"]["draw"] += 1

    return results


if __name__ == "__main__":
    print("Running bot vs bot experiments...")
    res = run_experiments(games=10, depth=4)
    print("\nResults:")
    print(res)
