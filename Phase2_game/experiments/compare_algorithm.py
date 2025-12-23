import time
from Phase2_game.game.board import create_board, print_board, PLAYER_MAX, PLAYER_MIN
from Phase2_game.game.logic import make_move
from Phase2_game.ai.minimax import minimax
from Phase2_game.ai.alphabeta import alphabeta


def run_experiment(depth=5):
    board = create_board()

    
    board = make_move(board, 3, PLAYER_MAX)
    board = make_move(board, 3, PLAYER_MIN)
    board = make_move(board, 2, PLAYER_MAX)
    board = make_move(board, 4, PLAYER_MIN)

    print("Testing on board:")
    print_board(board)

    
    mm_nodes = {"count": 0}
    t1 = time.time()
    score_mm, move_mm = minimax(board, depth, True, mm_nodes)
    t2 = time.time()

    
    ab_nodes = {"count": 0}
    t3 = time.time()
    score_ab, move_ab = alphabeta(board, depth, -999999, 999999, True, ab_nodes)
    t4 = time.time()

    print("\n--- RESULTS ---")
    print(f"Minimax: move={move_mm}, score={score_mm}, nodes={mm_nodes['count']}, time={t2-t1:.4f}s")
    print(f"AlphaBeta: move={move_ab}, score={score_ab}, nodes={ab_nodes['count']}, time={t4-t3:.4f}s")


if __name__ == "__main__":
    run_experiment(depth=5)
