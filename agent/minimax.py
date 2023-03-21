from .player import Player
import pdb

class Minimax(Player):
    def __init__(self, token, win_cnt):
        super().__init__(token, win_cnt)
        self.name = "Minimax"
        self.mbounds = self.win_cnt//2
        
        # updated every turn
        self.gameTree = {}
        self.rmin = None
        self.cmin = None
        self.rmax = None
        self.cmax = None

    # override
    def get_move(self, board, recent) -> tuple[int, int]:
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
        cache = self.gameTree.get(state.tobytes())
        if cache and cache[-1] == min_max:
            return cache[0]

        val = self.zs_eval(state)
        if val != None:
            return val
        elif depth == 0:
            return 0
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
   

