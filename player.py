from evaluation import Evaluator

class Player(object):
    def __init__(self, config, name, token):
        self.config = config
        self.name = name

        if token == 'white':
            self.color = (255,255,255)
            self.token = 1
            self.op_token = 2
        else:
            self.color = (0,0,0)
            self.token = 2
            self.op_token = 1

        self.evaluator = Evaluator(self.token, self.op_token)
        self.history = []
        self.win = False

    def set_move(self, curr_player, row, col, board):
        board.board[row][col] = curr_player.token
        if board.check_win(curr_player.token):
            return False, board
        else:
            return True, board

    def valid_move(self,row,col,board):
        if col > self.config.cols-1 or row > self.config.rows-1:
            print("Move out of bounds.")
            return False
        elif col < 0 or row < 0:
            print("Move out of bounds.")
            return False
        elif board.board[row][col] != 0:
            print("Move already placed...")
            return False
        else:
            self.history.append((row, col))
            return True

    # check for 3-3 rule (do this last)
    def check_33(self, token):
        pass













