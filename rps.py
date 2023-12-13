import os
import RPS_dict as rps
from prediction_agent import get_prediction_agent_action
from cicle_agent import Cicle_agent
from data_utils import store_data

def game():
        agent1_move = get_prediction_agent_action('RPS_dict')
        agent2_move = Cicle_agent.get_move('RPS_dict')
        result = rps.assess_game(agent1_move, agent2_move).name

        store_data(agent1_move, agent2_move, result)
        print('Agent 1 move is %s' % (rps.GameAction(agent1_move).name))
        print('Agent 2 move is %s' % (rps.GameAction(agent2_move).name))
        print(result)
        return result

if __name__ == '__main__':
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\t\t\033[1mROCK PAPER SCISSORS\033[0m')
        number_of_games = int(input('Input a number of games: '))
        for i in range(number_of_games):
            print('\n=====  \033[1;93mGAME %i\033[0m  =====' % (i + 1))
            game()
    except KeyboardInterrupt:
        print('\n\033[1;31mKeyBoard Interruption\033[0m')
        print('\n\033[1mBYE!\033[0m')