import argparse

def get_args():
    argp = argparse.ArgumentParser(description='Gomoku AI game', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argp.add_argument('--user', type = str, default = "O")
    argp.add_argument('--agent', type = str, default = "minimax")
    argp.add_argument('--cli', action = 'store_true')
    argp.add_argument('--rows', type = int, default = 3)
    argp.add_argument('--cols', type = int, default = 3)
    argp.add_argument('--cnt', type = int, default = 3)
    argp.add_argument('--window_x', type = int, default = 1300)
    argp.add_argument('--window_y', type = int, default = 1000)

    return argp.parse_args()
