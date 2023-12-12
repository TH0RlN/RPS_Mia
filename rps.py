import pandas as pd
import pathlib as p
import RPS_dict as rps
from random import choice

#History route
ROUTE = './src/'
HISTORY = './src/history.csv'

def get_data():
    file = p.Path(HISTORY)
    route = p.Path(ROUTE)

    if not route.is_dir():
         from os import mkdir
         mkdir(ROUTE)

    if file.is_file():
        return pd.read_csv(HISTORY)
    else:
        return pd.DataFrame(columns=('agent_move', 'rival_move', 'result'))

def store_data(agent_move, rival_move, result):
    data = get_data()
    data.loc[len(data)] = list((agent_move, rival_move, result))
    data.to_csv(HISTORY, index=False)


def get_agent_action():
    data = get_data()
    action = rps.GameAction(choice(range(len(rps.GameAction))))
    print('The agent action is %s' % (action.name))
    return action

def game():
        agent_move = get_agent_action()
        computer_move = rps.get_computer_action()
        result = rps.assess_game(agent_move, computer_move).name

        store_data(agent_move, computer_move, result)
        return result


if __name__ == '__main__':
    number_of_games = int(input('Input a number of games: '))
    for i in range(number_of_games):
        print('\n=====  \033[1;93mGAME %i\033[0m =====' % (i + 1))
        print(game())