# human player (not AI)

import numpy as np
import pdb

class Player(object):
    def __init__(self, token):
        self.name = "human"
        self.token = token
        self.recent = (None, None)


    def get_move(self, board):
        row_moves, col_moves = np.where(board == ".")
        assert len(row_moves) == len(col_moves)
        idx = np.random.choice(len(row_moves))
        return row_moves[idx], col_moves[idx]
         
