# Board class
import numpy as np
from tqdm import tqdm
import pdb


class Game(object):
    def __init__(self, config):
        self.config = config
        self.win_cnt = self.config.cnt
        self.rows = self.config.rows
        self.cols = self.config.cols
        self.board = np.array([['.']*self.rows for _ in range(self.cols)])
        self.gameLoop = True
        self.pywin = False
    
    
    def game_loop(self, p1, p2):
        self.print_board()
        while self.gameLoop:
            if np.sum(self.board == ".") == 0:
                self.gameLoop = False
                print("game tied...")
                return
            while True:
                ridx, cidx = p1.get_move(self.board, p2.recent)
                if self.valid_move(ridx, cidx):
                    self.board[ridx, cidx] = p1.token
                    self.print_board()
                    p1.recent = (ridx, cidx)
                    self.check_win(p1.token)
                    p1, p2 = p2, p1
                    break
        print(f"{p2.name} wins!")



    def start_cli_game(self, p1, p2, simulate = 0):
        print(f"Board size: {self.rows}x{self.cols}")
        print(f"{self.win_cnt} in-a-row wins the game.\n")
        self.game_loop(p1, p2)



    def start_gui_game(self, p1, p2):
        import pygame
        pygame.init()
        self.pywin = pygame.display.set_mode((self.config.window_x, self.config.window_y))
        pygame.display.set_caption("Alpha 오목")
        render_window = True
        curr_player = p1

        while True:
            self.render()
            self.blit_message(f"{curr_player.name}'s turn", msg_type = "turn")
            
            if curr_player.name == "human":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        render_window = False
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x_pos, y_pos = event.pos
                        cidx = x_pos//50 -1
                        ridx = y_pos//50 -1
            else:
                ridx, cidx = curr_player.get_move(self.board.copy())
            

            # TODO: for some reason pygame wont wait for user input
            pdb.set_trace()
            if self.valid_move(ridx, cidx):
                self.board[ridx][cidx] = curr_player.token
                res = self.check_win(curr_player.token)
                if res:
                    break
                else:
                    # switch player
                    curr_player = p2 if curr_player is p1 else p1
        
        # keep program alive till user quits
        while render_window:
            self.render()
            self.blit_message(f"{curr_player.name} wins!", msg_type = "win message")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    render_window = False
            pygame.display.update()
        self.terminate()


    def valid_move(self, row, col):
        if col > self.cols-1 or row > self.rows-1:
            print("Move out of bounds.")
            return False
        elif col < 0 or row < 0:
            print("Move out of bounds.")
            return False
        elif self.board[row,col] != ".":
            print("Move already taken...")
            return False
        else:
            return True
    
    def check_win(self, token):
        # Check rows
        for i in range(self.rows):
            for j in range(self.cols-self.win_cnt+1):
                if all(self.board[i][j+k] == token for k in range(self.win_cnt)):
                    self.gameLoop = False

        # Check columns
        for i in range(self.rows-self.win_cnt+1):
            for j in range(self.cols):
                if all(self.board[i+k][j] == token for k in range(self.win_cnt)):
                    self.gameLoop = False

        # Check diagonal (top-left to bottom-right)
        for i in range(self.rows-self.win_cnt+1):
            for j in range(self.cols-self.win_cnt+1):
                if all(self.board[i+k][j+k] == token for k in range(self.win_cnt)):
                    self.gameLoop = False

        # Check diagonal (bottom-left to top-right)
        for i in range(self.win_cnt-1, self.rows):
            for j in range(self.cols-self.win_cnt+1):
                if all(self.board[i-k][j+k] == token for k in range(self.win_cnt)):
                    self.gameLoop = False


    # TODO: check for 3-3 rule
    def check_33(self):
        pass
    
    
    def print_board(self):
        # easier to play
        print(" ", end = " ")
        for col in range(self.cols):
            print('{:2d}'.format(col), end = " ")
        print()
        
        for row in range(self.rows):
            print('{:2d}'.format(row), end = " ")
            for col in range(self.cols):
                print('{:2s}'.format(self.board[row,col]), end = " ")
            print()
        print()

    
    def render(self):
        self.pywin.fill([255, 178, 102])

        for i in range(1, self.rows+1):
            start_x = i*50
            start_y = 50
            end_y = 950
            pygame.draw.line(self.pywin, (0,0,0), (start_x, start_y), (start_x, end_y))

        for i in range(1, self.cols+1):
            start_x = 50
            start_y = i*50
            end_x = 950
            pygame.draw.line(self.pywin, (0,0,0), (start_x, start_y), (end_x, start_y))

        # draw points
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == "O":
                    x_pos = (j+1)*50 +25
                    y_pos = (i+1)*50 +25
                    pygame.draw.circle(self.pywin, (255, 255, 255), (x_pos, y_pos), 20, 0)
                elif self.board[i][j] == "X":
                    x_pos = (j+1)*50 +25
                    y_pos = (i+1)*50 +25
                    pygame.draw.circle(self.pywin, (0, 0, 0), (x_pos, y_pos), 20, 0)
   

    def blit_message(self, message, msg_type):
        myfont = pygame.font.SysFont("arial", 50)

        if msg_type == "welcome":
            text = myfont.render(message, False, (255, 255, 255), (0, 0, 0))
            self.pywin.blit(text, (1030, 50))

        elif msg_type == "win message":
            text = myfont.render(message, False, (255, 255, 255), (0, 0, 0))
            text_rect = text.get_rect()
            x, y = pygame.display.get_surface().get_size()
            text_rect.center = (x//2, y//2)
            self.pywin.blit(text, text_rect)

        elif msg_type == "turn":
            text = myfont.render(message, False, (0, 0, 0))
            self.pywin.blit(text, (970, 150))

        elif msg_type == "system message":
            font = pygame.font.SysFont("arial", 30)
            text = font.render(message, False, (255,255,255))
            self.pywin.blit(text, (970, 250))

    # quit pygame
    def terminate(self):
        pygame.display.quit()
        pygame.quit()
        print("Program successfully terminated.")



