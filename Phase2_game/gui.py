import tkinter as tk
import math
import time

from Phase2_game.game.board import *
from Phase2_game.game.logic import *
from Phase2_game.ai.minimax import minimax
from Phase2_game.ai.alphabeta import alphabeta
from Phase2_game.ai.random_bot import random_bot

CELL_SIZE = 80
ROWS_GUI = ROWS
COLS_GUI = COLS


def minimax_agent(board, depth):
    counter = {"count": 0}
    score, move = minimax(board, depth, True, counter)
    return move

def alphabeta_agent(board, depth):
    counter = {"count": 0}
    score, move = alphabeta(board, depth, -math.inf, math.inf, True, counter)
    return move

def random_agent(board, depth=None):
    return random_bot(board)



class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect-4 | Phase 2 AI")

        self.board = create_board()
        self.current_player = PLAYER_MAX
        self.depth = 4

        self.agent_max = None
        self.agent_min = None
        self.human_player = None
        self.running = False

        self.create_widgets()
        self.draw_board()


    def create_widgets(self):
        self.canvas = tk.Canvas(
            self.root,
            width=COLS_GUI * CELL_SIZE,
            height=ROWS_GUI * CELL_SIZE,
            bg="blue"
        )
        self.canvas.grid(row=0, column=0, columnspan=7)

        self.buttons = []
        for c in range(COLS_GUI):
            btn = tk.Button(
                self.root,
                text=str(c),
                command=lambda col=c: self.human_move(col),
                width=10
            )
            btn.grid(row=1, column=c)
            self.buttons.append(btn)

        self.status = tk.Label(self.root, text="Select Mode", font=("Arial", 14))
        self.status.grid(row=2, column=0, columnspan=7)

        # Mode selection
        tk.Button(self.root, text="Human vs Minimax",
                  command=lambda: self.start_game("HUMAN", "MINIMAX")).grid(row=3, column=0, columnspan=2)

        tk.Button(self.root, text="Human vs AlphaBeta",
                  command=lambda: self.start_game("HUMAN", "ALPHABETA")).grid(row=3, column=2, columnspan=2)

        tk.Button(self.root, text="Random vs Minimax",
                  command=lambda: self.start_game("RANDOM", "MINIMAX")).grid(row=3, column=4)

        tk.Button(self.root, text="Random vs AlphaBeta",
                  command=lambda: self.start_game("RANDOM", "ALPHABETA")).grid(row=3, column=5)

        tk.Button(self.root, text="Minimax vs AlphaBeta",
                  command=lambda: self.start_game("MINIMAX", "ALPHABETA")).grid(row=3, column=6)

   

    def start_game(self, p1, p2):
        self.board = create_board()
        self.current_player = PLAYER_MAX
        self.running = True

        
        self.player_max_name = p1
        self.player_min_name = p2

        self.status.config(text=f"{p1} vs {p2}")
        self.draw_board()

        self.agent_max = self.resolve_agent(p1)
        self.agent_min = self.resolve_agent(p2)

        self.human_player = PLAYER_MAX if p1 == "HUMAN" else PLAYER_MIN if p2 == "HUMAN" else None

        if self.human_player is None:
            self.root.after(500, self.ai_turn)


    def resolve_agent(self, name):
        if name == "MINIMAX":
            return minimax_agent
        if name == "ALPHABETA":
            return alphabeta_agent
        if name == "RANDOM":
            return random_agent
        return None

  

    def human_move(self, col):
        if not self.running:
            return
        if self.human_player != self.current_player:
            return
        if not is_valid_move(self.board, col):
            return

        self.make_move(col)

        
        if self.running and self.human_player != self.current_player:
            self.root.after(300, self.ai_turn)


    def ai_turn(self):
        if not self.running:
            return

        if is_terminal(self.board):
            self.end_game()
            return

        agent = self.agent_max if self.current_player == PLAYER_MAX else self.agent_min
        if agent is None:
            return  

        move = agent(self.board, self.depth)
        self.make_move(move)

        
        if self.running and self.human_player is None:
            self.root.after(300, self.ai_turn)


            if self.human_player is None:
                self.root.after(500, self.ai_turn)

    def make_move(self, col):
        self.board = make_move(self.board, col, self.current_player)
        self.current_player = PLAYER_MIN if self.current_player == PLAYER_MAX else PLAYER_MAX
        self.draw_board()

        if is_terminal(self.board):
            self.end_game()


    

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(ROWS_GUI):
            for c in range(COLS_GUI):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                piece = self.board[r][c]

                color = "white"
                if piece == PLAYER_MAX:
                    color = "red"
                elif piece == PLAYER_MIN:
                    color = "yellow"

                self.canvas.create_oval(
                    x1 + 10, y1 + 10, x2 - 10, y2 - 10,
                    fill=color
                )

    

    def end_game(self):
        self.running = False
        winner = check_winner(self.board)

        if winner == PLAYER_MAX:
            self.status.config(text=f"{self.player_max_name} wins!")
        elif winner == PLAYER_MIN:
            self.status.config(text=f"{self.player_min_name} wins!")
        else:
            self.status.config(text="Draw!")





if __name__ == "__main__":
    root = tk.Tk()
    app = Connect4GUI(root)
    root.mainloop()
