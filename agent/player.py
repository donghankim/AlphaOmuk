# human player (not AI)

import numpy as np
import pdb

class Player(object):
    def __init__(self, token, win_cnt):
        self.name = "human"
        self.token = token
        self.win_cnt = win_cnt
        self.recent = (None, None)

    
    def get_move(self, *args) -> tuple[int, int]:
        assert self.name == "human", "AI forgot to override get_move()"
        pos_in = list(map(int, input("You play (row,col): ").split()))
        ridx, cidx = pos_in[0], pos_in[1]
        return ridx, cidx
        

    def random_move(self, board) -> tuple[int, int]:
        row_moves, col_moves = np.where(board == ".")
        assert len(row_moves) == len(col_moves)
        idx = np.random.choice(len(row_moves))
        return row_moves[idx], col_moves[idx]
         
