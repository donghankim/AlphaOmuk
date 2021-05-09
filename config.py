import argparse

def get_args():
    argp = argparse.ArgumentParser(description='Gomoku AI game', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    argp.add_argument('--debug', action = 'store_true')
    argp.add_argument('--no_gui', action = 'store_true')
    argp.add_argument('--window_x', type = int, default = 1300)
    argp.add_argument('--window_y', type = int, default = 1000)
    argp.add_argument('--rows', type = int, default = 19)
    argp.add_argument('--cols', type = int, default = 19)

    return argp.parse_args()
