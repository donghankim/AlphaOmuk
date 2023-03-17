 # export PYTHONPATH=$(pwd)

from config import get_args
from game import Game
import agent


def main():
    config = get_args()
    if config.user == "O":
        hp = agent.Player(token = "O", win_cnt = config.cnt)
        ai = agent.Minimax(token = "X", win_cnt = config.cnt)
        game = Game(config)
        game.start_cli_game(hp, ai) if config.cli else game.start_gui_game(hp, ai)
    else:
        hp = agent.Player(token = "X", win_cnt = config.cnt)
        ai = agent.Minimax(token = "O", win_cnt = config.cnt)
        game = Game(config)
        game.start_cli_game(ai, hp) if config.cli else game.start_gui_game(ai, hp)


if __name__ == '__main__':
    main()

