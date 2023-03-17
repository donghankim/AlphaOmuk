from .player import Player
from utils import *
import numpy as np
import re, math
import pdb


# TODO:
# I think there is something wrong with how I am recursing minimax. best_state seems to be
# being shared by the recursive calls...


# O: Max token, X: Min token
class Minimax(Player):
    def __init__(self, token, win_cnt):
        super().__init__(token, win_cnt)
        self.name = "Minimax"
        self.mbounds = 2
        
        # updated every turn
        self.gameTree = None
        self.rows = None
        self.cols = None
        self.rmin = None
        self.cmin = None
        self.rmax = None
        self.cmax = None

        self.temp = []
        

    def get_move(self, board, recent) -> tuple[int, int]:
        self.gameTree = {}
        self.rows, self.cols = board.shape
        self.update_bounds(recent)
        
        if self.token == "O":
            qval = self.minimax(board, min_max = "max")
            ridx, cidx = self.gameTree[board.tobytes()][1]
        else:
            qval = self.minimax(board, min_max = "min")
            ridx, cidx = self.gameTree[board.tobytes()][1]
        
        print(f"{self.name} plays (row, col):", ridx, cidx)
        return ridx, cidx
    
    
    def minimax(self, state, alpha = float('-inf'), beta = float('inf'), depth = 100, min_max = "min"):
        val = self.zs_eval(state)
        if val != None:
            return val
        else:
            pos_states = self.get_states(state, "O") if min_max == "max" else self.get_states(state, "X")
            best_val = float('inf') if min_max == "min" else float('-inf')
            best_action = None

            for at, st in pos_states:
                if min_max == "max":
                    val = self.minimax(st, alpha, beta, depth = depth-1, min_max = "min")
                    if val > best_val:
                        best_val = val
                        best_action = at
                        alpha = max(alpha, best_val)
                    if best_val >= beta:
                        return best_val
                
                elif min_max == "min":
                    val = self.minimax(st, alpha, beta, depth = depth-1, min_max = "max")
                    if val < best_val:
                        best_val = val
                        best_action = at
                        beta = min(beta, best_val)
                    if best_val <= alpha:
                        return best_val
            
            self.gameTree[state.tobytes()] = (best_val, best_action, min_max)
            return best_val
   

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
            

    def get_states(self, board, token, random = False):
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

