from .player import Player
from utils import *
import numpy as np
import pdb

class MCTS(Player):
    def __init__(self, token, win_cnt):
        super().__init__(token, win_cnt)
        self.name = "MCTS"
        self.gameTree = {}


    def get_move(self, board, recent) -> tuple[int, int]:
        self.rows, self.cols = board.shape
        return 0, 0

