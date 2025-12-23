import random
from Phase2_game.game.logic import get_valid_moves

def random_bot(board):
    moves = get_valid_moves(board)
    return random.choice(moves)
