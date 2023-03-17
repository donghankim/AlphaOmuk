import numpy as np
import re

class State:
    def __init__(self, board = None, action = None, val = None):
        self.board = board
        self.action = action
        self.val = val
    
    @staticmethod
    def get_action(st):
        if st.parent.parent == None:
            return st.action
        else:
            return State.get_action(st.parent)

    @staticmethod
    def print_sim(st):
        if st:
            print(st.board, end=" ")
            print(st.val)
            State.print_sim(st.parent)
            



