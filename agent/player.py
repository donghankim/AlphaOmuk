# human player (not AI)

import numpy as np
import re
import pdb


# O: Max token, X: Min token
class Player(object):
    def __init__(self, token, win_cnt):
        self.name = "human"
        self.token = token
        self.win_cnt = win_cnt
        self.rows = None
        self.cols = None
        self.recent = (None, None)
        

    
    # all AI class must override
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
    
    def update_bounds(self, recent):
        prev_row, prev_col = recent
        if prev_row and prev_col:
            rmin = max(0, prev_row-self.mbounds)
            rmax = min(self.rows-1, prev_row+self.mbounds)
            cmin = max(0, prev_col-self.mbounds)
            cmax = min(self.cols-1, prev_col+self.mbounds)
        else:
            rmin = max(0, self.rows//2 - self.mbounds)
            rmax = min(self.rows-1, self.rows//2 + self.mbounds)
            cmin = max(0, self.cols//2 - self.mbounds)
            cmax = min(self.cols-1, self.cols//2 + self.mbounds)
        
        if rmax - rmin <= self.mbounds:
            rmax = min(rmax+2, self.rows-1)
        if cmax - cmin <= self.mbounds:
            cmax = min(cmax+2, self.cols-1)

        self.rmin = rmin; self.rmax = rmax
        self.cmin = cmin; self.cmax = cmax
            

    def get_states(self, board, token, random = True):
        states = []
        avail = np.where(board == ".")
        actions = list(filter(lambda x: ((self.rmin <= x[0] <= self.rmax) and (self.cmin <= x[1] <= self.cmax)), zip(avail[0], avail[1])))
        if random:
            np.random.shuffle(actions)
        
        for i in range(len(actions)):
            row, col = actions[i]
            new_state = board.copy()
            new_state[row, col] = token
            states.append((actions[i], new_state))
        
        return states

    # zero sum utility
    def zs_eval(self, state):
        def k_in_row(state, regex):
            # Return a list of all consecutive board positions in state that satisfy regex
            flipped = np.fliplr(state)
            sequences = []

            for i in range(state.shape[0]):
                sequences.extend(re.findall(regex, "".join(state[i])))
                sequences.extend(re.findall(regex, "".join(np.diag(state, k=-i))))
                sequences.extend(re.findall(regex, "".join(np.diag(flipped, k=-i))))
            for j in range(state.shape[1]):
                sequences.extend(re.findall(regex, "".join(state[:, j])))
                if j != 0:
                    sequences.extend(re.findall(regex, "".join(np.diag(state, k=j))))
                    sequences.extend(re.findall(regex, "".join(np.diag(flipped, k=j))))
            return sequences

        empty_sq = np.sum(state == ".")
        if k_in_row(state, "X{" + str(self.win_cnt) + "}"):
            return -1*(empty_sq+1)
        elif k_in_row(state, "O{" + str(self.win_cnt) + "}"):
            return (empty_sq+1)
        elif empty_sq == 0:
            return 0
        else:
            # non-terminal
            return None

    
    # for debug (print use)
    def convert(self, state):
        return np.frombuffer(state, dtype = '<U1').reshape(3,3)
         
