from config import get_args
import numpy as np
import pygame
from player import Player
from board import Board
import agent
import pdb


"""
TO DO:
1. agent does not recognize player moves (doesnt show in state graph)
2. check to see if eval if doing well
3. Implemented a way to evaluate opponents moves as well (self.op_token)
"""


# for quiting application
def terminate():
    pygame.display.quit()
    pygame.quit()
    print("Program successfully terminated.")


# for displaying messages
def blit_message(window, message, kind):
    myfont = pygame.font.SysFont("arial", 50)

    if kind == "welcome":
        text = myfont.render(message, False, (255, 255, 255), (0, 0, 0))
        window.blit(text, (1030, 50))

    elif kind == "win message":
        text = myfont.render(message, False, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        x, y = pygame.display.get_surface().get_size()
        text_rect.center = (x//2, y//2)
        window.blit(text, text_rect)

    elif kind == "turn":
        text = myfont.render(message, False, (0, 0, 0))
        window.blit(text, (970, 150))

    elif kind == "system message":
        font = pygame.font.SysFont("arial", 30)
        text = font.render(message, False, (255,255,255))
        window.blit(text, (970, 250))

# to display the board
def basic_window(window, board):
    window.fill([255, 178, 102])
    blit_message(window, "Gomoku", "welcome")
    board.draw_board(window)

def switch_player(p1, p2):
    temp = p1
    p1 = p2
    p2 = temp
    return p1, p2

def main():
    program_run = True
    config = get_args()
    board = Board(config)
    p1 = Player(config, 'player 1', 'white')
    # p2 = Player(config, 'player 2', 'black')
    # p2 = agent.Naiive(config, 'computer', 'black')
    p2 = agent.Heuristic(config, 'computer', 'black')
    curr_player = p1
    wait_player = p2

    # debug
    if config.debug:
        board.set_board()
        row_board, col_board = p2.make_move(p2, board)

    # no gui play
    if config.no_gui:
        while board.game_run:
            print(board.board)
            if curr_player.name == 'computer':
                row_board, col_board = curr_player.make_move(curr_player, board)
                board.game_run = curr_player.set_move(curr_player, row_board, col_board, board)
                if board.game_run:
                    curr_player, wait_player = switch_player(curr_player, wait_player)
            else:
                pos_in = list(map(int, input("Enter points: ").split()))
                row_board, col_board = pos_in[0], pos_in[1]
                if curr_player.valid_move(row_board, col_board, board):
                    board.game_run = curr_player.set_move(curr_player, row_board, col_board, board)
                    if board.game_run:
                        curr_player, wait_player = switch_player(curr_player, wait_player)

    # pygame application (GUI enabled)
    else:
        pygame.init()
        window = pygame.display.set_mode((config.window_x, config.window_y))
        pygame.display.set_caption("Gomoku AI")
        clock = pygame.time.Clock()

        # Game loop
        while board.game_run:
            basic_window(window, board)
            blit_message(window, f"{curr_player.name}'s turn", "turn")

            if curr_player.name == 'computer':
                row_board, col_board = curr_player.make_move(curr_player, wait_player, board)
                board.game_run = curr_player.set_move(curr_player, row_board, col_board, board)
                if board.game_run:
                    curr_player, wait_player = switch_player(curr_player, wait_player)

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        board.game_run = False
                        terminate()
                        return

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x_pos, y_pos = event.pos
                        col_board = abs(round(x_pos/50) - 1)
                        row_board = abs(round(y_pos/50) - 1)
                        if curr_player.valid_move(row_board, col_board, board):
                            board.game_run = curr_player.set_move(curr_player, row_board, col_board, board)
                            if board.game_run:
                                curr_player, wait_player = switch_player(curr_player, wait_player)

            pygame.display.update()

        # Game terminated
        while program_run:
            basic_window(window, board)
            blit_message(window, f"{curr_player.name} wins!", "win message")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    program_run = False
                    break

            pygame.display.update()

        terminate()
        return


if __name__ == '__main__':
    main()

