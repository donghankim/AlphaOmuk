# Board class
import numpy as np
import pygame
import pdb

class Board(object):
    def __init__(self, config):
        self.config = config
        self.rows = 19
        self.cols = 19
        self.win_count = 5
        self.board = np.array([[0] * self.rows] * self.cols)
        self.game_run = True

        if config.debug:
            self.set_board()

    def check_win(self, token):
        # check horizontal
        for i in range(self.cols):
            for j in range(self.rows - self.win_count +1):
                if self.board[i][j] == token and self.board[i][j+1] == token and self.board[i][j+2] == token and self.board[i][j+3] == token and self.board[i][j+4] == token:
                    return True

        # check vertical
        for i in range(self.cols - self.win_count + 1):
            for j in range(self.rows):
                if self.board[i][j] == token and self.board[i+1][j] == token and self.board[i+2][j] == token and self.board[i+3][j] == token and self.board[i+4][j] == token:
                    return True

        # check negative diagonal
        for i in range(self.win_count-1, self.cols):
            for j in range(self.win_count-1, self.rows):
                if self.board[i][j] == token and self.board[i-1][j-1] == token and self.board[i-2][j-2] == token and self.board[i-3][j-3] == token and self.board[i-4][j-4] == token:
                    return True

        #check positive diagonal
        for i in range(self.win_count-1, self.cols):
            for j in range(self.rows - self.win_count-1):
                if self.board[i][j] == token and self.board[i-1][j+1] == token and self.board[i-2][j+2] == token and self.board[i-3][j+3] == token and self.board[i-4][j+4] == token:
                    return True


    def draw_board(self, window):
        # draw board
        for i in range(1,self.config.rows+1):
            start_x = i*50
            start_y = 50
            end_y = 950
            pygame.draw.line(window, (0,0,0), (start_x, start_y), (start_x, end_y))

        for i in range(1,self.config.cols+1):
            start_x = 50
            start_y = i*50
            end_x = 950
            pygame.draw.line(window, (0,0,0), (start_x, start_y), (end_x, start_y))

        # draw points
        for i in range(self.config.rows):
            for j in range(self.config.cols):
                if self.board[i][j] == 1:
                    x_pos = (j+1)*50
                    y_pos = (i+1)*50
                    pygame.draw.circle(window, (255, 255, 255), (x_pos, y_pos), 12, 0)
                elif self.board[i][j] == 2:
                    x_pos = (j+1)*50
                    y_pos = (i+1)*50
                    pygame.draw.circle(window, (0, 0, 0), (x_pos, y_pos), 12, 0)


    # for debugging purposes
    def set_board(self):
        self.board[5][5] = 2
        self.board[5][6] = 2
        self.board[5][7] = 2
        self.board[4][5] = 2
        self.board[3][5] = 2



