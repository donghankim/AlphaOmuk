from config import get_args
from game import Game
import agent



def main():
    config = get_args()
    hp = agent.Player(token = "O")
    ai = agent.Minimax(token = "X")
    game = Game(config)
    game.cli_game_loop(hp, ai) if config.cli else game.gui_game_loop(hp, ai)
    


if __name__ == '__main__':
    main()

