from player import Player
import numpy as np
import random
from copy import deepcopy
import pdb


class Naiive(Player):
    def __init__(self, config, name, token):
        super().__init__(config, name, token)

    def make_move(self, curr_player, wait_player, board):
        recent_x = wait_player.history[-1][0]
        recent_y = wait_player.history[-1][1]

        while True:
            random_x = random.randint(recent_x-1, recent_x+1)
            random_y = random.randint(recent_y-1, recent_y+1)
            if self.valid_move(random_x, random_y, board):
                return random_x, random_y


class Heuristic(Player):
    def __init__(self, config, name, token):
        super().__init__(config, name, token)
        self.north_score = 0
        self.east_score = 0
        self.south_score = 0
        self.west_score = 0
        self.ne_score = 0
        self.se_score = 0
        self.sw_score = 0
        self.nw_score = 0

    def make_move(self, curr_player, wait_player, board):
        recent_x = wait_player.history[-1][0]
        recent_y = wait_player.history[-1][1]

        # create search area
        states = np.zeros_like(board.board)
        for row in range(board.board.shape[0]):
            for col in range(board.board.shape[1]):
                if board.board[row][col] == curr_player.token:
                    states[row][col] = -1*curr_player.token
                elif board.board[row][col] == wait_player.token:
                    states[row][col] = -1*wait_player.token
                else:
                    states[row][col] = self.evaluator.evaluate(row, col, states)

        print(board.board)
        print(states)
        max_idx = np.unravel_index(states.argmax(), states.shape)
        row_move = max_idx[0]
        col_move = max_idx[1]

        while True:
            if self.valid_move(row_move, col_move, board):
                break
            else:
                row_move += 1

        return row_move, col_move
