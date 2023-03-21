 # export PYTHONPATH=$(pwd)

from config import get_args
from game import Game
import agent

def main():
    config = get_args()

    if config.user == "O":
        human_token = "O"
        ai_token = "X"
    else:
        human_token = "X"
        ai_token = "O"

    human = agent.Player(token = human_token, win_cnt = config.cnt)
    if config.agent == "minimax":
        ai = agent.Minimax(token = ai_token, win_cnt = config.cnt)
    elif config.agent == "mcts":
        ai = agent.MCTS(token = ai_token, win_cnt = config.cnt)
    elif config.agent == "policy":
        ai = agent.Policy(token = ai_token, win_cnt = config.cnt)
    elif config.argent == "sarsa":
        ai = agent.SARSA(token = ai_token, win_cnt = config.cnt)
    else:
        print("error in main")
        return

    game = Game(config) 
    game.start_cli_game(human, ai) if config.cli else game.start_gui_game(human, ai)


if __name__ == '__main__':
    main()

