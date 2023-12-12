import pandas as pd
import pathlib as p
import RPS_dict as rps
from random import choice
from data_utils import get_data, store_data


def get_agent_action():
    data = get_data()

    last_game = data.tail(1)
    similar_games = data.loc[(data['agent_move'] == last_game['agent_move'].iloc[0]) & (data['rival_move'] == last_game['rival_move'].iloc[0])]
    next_indexes = list(filter(lambda y: y < len(data), list(map(lambda x: x+1 , list(similar_games.index)))))
    next_games = data.iloc[next_indexes]
    next_rival = next_games['rival_move']
    print(next_rival.value_counts())


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