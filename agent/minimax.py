import pdb
from .player import Player

class Minimax(Player):
    def __init__(self, token):
        self.name = "Minimax"
        self.token = token
        self.alpha = float('inf')
        self.beta = float('-inf')

    
    # def get_move(self, board):
    #     pass




