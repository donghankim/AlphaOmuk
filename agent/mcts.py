from .player import Player
import numpy as np
import math, random
import pdb


class State:
    def __init__(self, parent = None, action = None, val = None, token = None):
        self.parent = parent 
        self.token = token
        self.action = action
        self.val = val
        self.N = 1
        self.W = 0
        


class MCTS(Player):
    def __init__(self, token, win_cnt):
        super().__init__(token, win_cnt)
        self.name = "MCTS"
        self.gameTree = {}
        self.alpha = math.sqrt(2)
        self.runs = 500
        self.op_token = "O" if self.token == "X" else "X"
        self.mbounds = self.win_cnt


    def get_move(self, board, recent) -> tuple[int, int]:
        self.rows, self.cols = board.shape
        self.update_bounds(recent)
        self.gameTree = {}

        cnt = 0
        while cnt < self.runs:
            expand_state = self.select(board.copy())
            sim_state = self.expand(expand_state)
            res = self.simulate(sim_state)
            self.backprop(sim_state, res)
            cnt += 1
        
        res = sorted(self.gameTree.values(), key = lambda x:x.W, reverse = True)
        for qa in res:
            if qa.token == self.token:
                ridx, cidx = qa.action
                break

        print(f"{self.name} plays (row, col):", ridx, cidx)
        return ridx, cidx
    

    def select(self, state):
        val = self.zs_eval(state)
        if val == None:
            cached = self.gameTree.get(state.tobytes())
            if cached == None:
                NS = State(token = self.op_token)
                self.gameTree[state.tobytes()] = NS
                return state
            else:
                PS = self.gameTree[state.tobytes()]
                tk = "O" if cached.token == "X" else "X"
                best_utc = float('-inf')
                best_state = None
                pos_states = self.get_states(state, tk)

                for at, st in pos_states:
                    S = self.gameTree.get(st.tobytes())
                    if S:
                        utc = self.calc_utc(S)
                        if utc > best_utc:
                            best_utc = utc
                            best_state = st
                    else:
                        self.gameTree[st.tobytes()] = State(parent = PS, action = at, token = tk)
                        return st

                return state if best_state is None else best_state
        else:
            return state
    

    def expand(self, state):
        val = self.zs_eval(state)
        if val != None:
            return state

        S = self.gameTree[state.tobytes()]
        tk = "O" if S.token == "X" else "X"
        PS = self.gameTree[state.tobytes()]
        pos_states = self.get_states(state, tk)

        for at, st in pos_states:
            if self.gameTree.get(st.tobytes()) == None:
                self.gameTree[st.tobytes()] = State(parent = PS, action = at, token = tk)
                return st
        return state


    def simulate(self, state):
        token = self.gameTree[state.tobytes()].token
        while self.zs_eval(state) == None:
            token = "O" if token == "X" else "X"
            pos_states = self.get_states(state, token)
            _, state = random.choice(pos_states)

        return self.zs_eval(state)



    def backprop(self, state, res):
        S = self.gameTree.get(state.tobytes())
        while S is not None:
            S.N += 1
            if res == 0:
                S.W += 0.5
            elif (S.token == "X" and res < 0) or (S.token == "O" and res > 0):
                S.W += 1
            S = S.parent

    
    def calc_utc(self, S):
        if S.parent == None:
            return S.W/S.N
        else:
            utc = (S.W/S.N) + self.alpha*math.sqrt(math.log(S.parent.N)/S.N)
            return utc
