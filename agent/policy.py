from .player import Player
import numpy as np
import pdb

class Policy(Player): 
    def __init__(self, token, win_cnt):
        self.name = "policy iteration (dp)"
    
    def get_move(self, board, recent) -> tuple[int, int]:
        return 0, 0
    


