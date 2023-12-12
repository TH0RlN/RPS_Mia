import RPS_dict as rps
from prediction_agent import get_prediction_agent_action
from cicle_agent import Cicle_agent
from data_utils import store_data

def game():
        agent_move = get_prediction_agent_action()
        computer_move = Cicle_agent.get_move()
        result = rps.assess_game(agent_move, computer_move).name

        store_data(agent_move, computer_move, result)
        return result

if __name__ == '__main__':
    number_of_games = int(input('Input a number of games: '))
    for i in range(number_of_games):
        print('\n=====  \033[1;93mGAME %i\033[0m =====' % (i + 1))
        print(game())