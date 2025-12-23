import math
from graphviz import Digraph
import os
from Phase2_game.game.logic import (
    get_valid_moves,
    make_move,
    is_terminal,
    check_winner,
)
from Phase2_game.game.board import PLAYER_MAX, PLAYER_MIN
from Phase2_game.ai.evaluation import evaluate_board


class TreeNode:
    def __init__(self, move=None, player=None, depth=0):
        self.move = move
        self.player = player
        self.depth = depth

        self.score = None
        self.children = []
        self.pruned = False

    def add_child(self, child):
        self.children.append(child)



def print_tree(node, indent=0):
    prefix = "│   " * indent
    prune = " ✂️" if node.pruned else ""
    print(
        f"{prefix}Move={node.move}, "
        f"Player={node.player}, "
        f"Score={node.score}{prune}"
    )
    for child in node.children:
        print_tree(child, indent + 1)


def visualize_tree(root, filename):
     # Create output directory if it doesn't exist
    output_dir = "output_image"
    os.makedirs(output_dir, exist_ok=True)

    # Full path without extension
    full_path = os.path.join(output_dir, filename)

    dot = Digraph(comment="Search Tree")

    def visit(node, parent_id=None):
        node_id = str(id(node))
        label = (
            f"Move: {node.move}\n"
            f"Player: {node.player}\n"
            f"Score: {node.score}"
        )
        if node.pruned:
            label += "\nPRUNED"

        dot.node(node_id, label)

        if parent_id:
            dot.edge(parent_id, node_id)

        for c in node.children:
            visit(c, node_id)

    visit(root)
    dot.render(full_path, format="png", cleanup=True)

def minimax_tree(board, depth, maximizing_player, node_counter, tree_node):
    node_counter["count"] += 1

    winner = check_winner(board)
    if depth == 0 or is_terminal(board):
        if winner == PLAYER_MAX:
            tree_node.score = 10000
        elif winner == PLAYER_MIN:
            tree_node.score = -10000
        else:
            tree_node.score = evaluate_board(board, PLAYER_MAX)
        return tree_node.score, None

    valid_moves = get_valid_moves(board)

    if maximizing_player:
        value = -math.inf
        best = None

        for col in valid_moves:
            child_board = make_move(board, col, PLAYER_MAX)

            child_node = TreeNode(
                move=col,
                player=PLAYER_MAX,
                depth=tree_node.depth + 1
            )
            tree_node.add_child(child_node)

            new_score, _ = minimax_tree(
                child_board,
                depth - 1,
                False,
                node_counter,
                child_node
            )

            if new_score > value:
                value = new_score
                best = col

        tree_node.score = value
        return value, best

    else:
        value = math.inf
        best = None

        for col in valid_moves:
            child_board = make_move(board, col, PLAYER_MIN)

            child_node = TreeNode(
                move=col,
                player=PLAYER_MIN,
                depth=tree_node.depth + 1
            )
            tree_node.add_child(child_node)

            new_score, _ = minimax_tree(
                child_board,
                depth - 1,
                True,
                node_counter,
                child_node
            )

            if new_score < value:
                value = new_score
                best = col

        tree_node.score = value
        return value, best


def alphabeta_tree(board, depth, alpha, beta, maximizing_player, node_counter, tree_node):
    node_counter["count"] += 1

    winner = check_winner(board)
    if depth == 0 or is_terminal(board):
        if winner == PLAYER_MAX:
            tree_node.score = 10000
        elif winner == PLAYER_MIN:
            tree_node.score = -10000
        else:
            tree_node.score = evaluate_board(board, PLAYER_MAX)
        return tree_node.score, None

    valid_moves = get_valid_moves(board)

    if maximizing_player:
        value = -math.inf
        best = None

        for col in valid_moves:
            child_board = make_move(board, col, PLAYER_MAX)

            child_node = TreeNode(
                move=col,
                player=PLAYER_MAX,
                depth=tree_node.depth + 1
            )
            tree_node.add_child(child_node)

            new_score, _ = alphabeta_tree(
                child_board,
                depth - 1,
                alpha,
                beta,
                False,
                node_counter,
                child_node
            )

            if new_score > value:
                value = new_score
                best = col

            alpha = max(alpha, value)
            if alpha >= beta:
                child_node.pruned = True
                break  #  pruning

        tree_node.score = value
        return value, best

    else:
        value = math.inf
        best = None

        for col in valid_moves:
            child_board = make_move(board, col, PLAYER_MIN)

            child_node = TreeNode(
                move=col,
                player=PLAYER_MIN,
                depth=tree_node.depth + 1
            )
            tree_node.add_child(child_node)

            new_score, _ = alphabeta_tree(
                child_board,
                depth - 1,
                alpha,
                beta,
                True,
                node_counter,
                child_node
            )

            if new_score < value:
                value = new_score
                best = col

            beta = min(beta, value)
            if alpha >= beta:
                child_node.pruned = True
                break  # ✂️ pruning

        tree_node.score = value
        return value, best
