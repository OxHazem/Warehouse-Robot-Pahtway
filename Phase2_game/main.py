from Phase2_game.game.board import *
from Phase2_game.game.logic import *
from Phase2_game.ai.minimax import minimax
from Phase2_game.ai.alphabeta import alphabeta


def play(depth=4, use_alpha_beta=True):
    board = create_board()
    current = PLAYER_MAX  

    while True:
        print_board(board)

        if is_terminal(board):
            winner = check_winner(board)
            if winner == PLAYER_MAX:
                print("AI wins!")
            elif winner == PLAYER_MIN:
                print("Human wins!")
            else:
                print("Draw!")
            break

        if current == PLAYER_MAX:
            print("AI thinking...")

            node_counter = {"count": 0}
            if use_alpha_beta:
                score, move = alphabeta(board, depth, -99999, 99999, True, node_counter)
            else:
                score, move = minimax(board, depth, True, node_counter)

            print(f"AI chooses column {move} (nodes={node_counter['count']})")
            board = make_move(board, move, PLAYER_MAX)
            current = PLAYER_MIN

        else:
            col = int(input("Your move (0–6): "))
            if not is_valid_move(board, col):
                print("Invalid move, try again.")
                continue
            board = make_move(board, col, PLAYER_MIN)
            current = PLAYER_MAX


if __name__ == "__main__":
    play(depth=4, use_alpha_beta=True)
