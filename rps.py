import pandas as pd
import pathlib as pl
import RPS_dict as rps
from random import choice

def get_agent_action():
    action = rps.GameAction(choice(range(len(rps.GameAction))))
    print('The agent action is %s' % (action.name))
    return action

if __name__ == '__main__':
    number_of_games = int(input('Input a number of games: '))
    for i in range(number_of_games):
        print('=====  \033[1;93mGAME %i\033[0m =====' % (i))
        agent_move = get_agent_action()
        computer_move = rps.get_computer_action()
        rps.assess_game(agent_move, computer_move)