import time
import math
from Phase2_game.game.board import create_board, print_board, PLAYER_MAX, PLAYER_MIN
from Phase2_game.game.logic import make_move, is_terminal, check_winner
from Phase2_game.ai.minimax import minimax
from Phase2_game.ai.alphabeta import alphabeta
from Phase2_game.ai.random_bot import random_bot
from Phase2_game.ai.search_tree import (
    TreeNode,
    minimax_tree,
    alphabeta_tree,
    visualize_tree,
)




def minimax_ai_with_stats(board, depth):
    node_counter = {"count": 0}
    start = time.time()
    score, move = minimax(board, depth, True, node_counter)
    end = time.time()
    return move, node_counter["count"], end - start


def alphabeta_ai_with_stats(board, depth):
    node_counter = {"count": 0}
    start = time.time()
    score, move = alphabeta(board, depth, -math.inf, math.inf, True, node_counter)
    end = time.time()
    return move, node_counter["count"], end - start


def random_ai_with_stats(board, depth=None):
    start = time.time()
    move = random_bot(board)
    end = time.time()
    return move, 1, end - start   




def play_match(
    ai1, ai1_name,
    ai2, ai2_name,
    depth=4,
    verbose=False,
    visualize=False
):
    board = create_board()
    current_player = PLAYER_MAX
    move_stats = []

    MAX_MOVES = 42

    for move_index in range(MAX_MOVES):

        if is_terminal(board):
            winner = check_winner(board)
            return winner, move_stats


        if current_player == PLAYER_MAX:

            if visualize and ai1.__name__.endswith("_with_tree"):
                move, nodes, duration = ai1(
                    board,
                    depth,
                    f"{ai1_name}_move_{move_index}"
                )
            else:
                move, nodes, duration = ai1(board, depth)

            board = make_move(board, move, PLAYER_MAX)
            move_stats.append((ai1_name, move, nodes, duration))
            current_player = PLAYER_MIN


        else:

            if visualize and ai2.__name__.endswith("_with_tree"):
                move, nodes, duration = ai2(
                    board,
                    depth,
                    f"{ai2_name}_move_{move_index}"
                )
            else:
                move, nodes, duration = ai2(board, depth)

            board = make_move(board, move, PLAYER_MIN)
            move_stats.append((ai2_name, move, nodes, duration))
            current_player = PLAYER_MAX

        if verbose:
            print_board(board)

    return None, move_stats





def run_comparison(depth=4):
    print("\n--- MINIMAX vs RANDOM ---")
    winner, stats = play_match(
        minimax_ai_with_tree, "Minimax",
        random_ai_with_stats, "Random",
        depth=3,
        verbose=False,
        visualize=True
    )
    print_results(stats, winner)

    print("\n--- ALPHABETA vs RANDOM ---")
    winner, stats = play_match(
        alphabeta_ai_with_tree, "AlphaBeta",
        random_ai_with_stats, "Random",
        depth=3,
        verbose=False,
        visualize=True
    )
    print_results(stats, winner)



def minimax_ai_with_tree(board, depth, tree_name="minimax_tree"):
    node_counter = {"count": 0}
    root = TreeNode(move="ROOT", player=PLAYER_MAX)

    start = time.time()
    score, move = minimax_tree(
        board, depth, True, node_counter, root
    )
    end = time.time()

    visualize_tree(root, tree_name)

    return move, node_counter["count"], end - start


def alphabeta_ai_with_tree(board, depth, tree_name="alphabeta_tree"):
    node_counter = {"count": 0}
    root = TreeNode(move="ROOT", player=PLAYER_MAX)

    start = time.time()
    score, move = alphabeta_tree(
        board, depth, -math.inf, math.inf, True, node_counter, root
    )
    end = time.time()

    visualize_tree(root, tree_name)

    return move, node_counter["count"], end - start


def print_results(stats, winner):
    print("\nMove-by-move statistics:")
    print("Player\tMove\tNodes Expanded\tTime (s)")

    total_nodes = 0
    total_time = 0

    for player, move, nodes, duration in stats:
        total_nodes += nodes
        total_time += duration
        print(f"{player}\t{move}\t{nodes}\t\t{duration:.4f}")

    print("\nFinal Winner:", "AI" if winner == PLAYER_MAX else "Random" if winner == PLAYER_MIN else "Draw")
    print("Total Nodes Expanded:", total_nodes)
    print("Total Time:", f"{total_time:.4f}s")


if __name__ == "__main__":
    run_comparison(depth=4)
