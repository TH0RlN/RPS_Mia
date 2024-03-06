from random import choice
from data_utils import get_data

# Given a game and a predicted move, it returns the best move against it
def get_victory_action(move, game):
    rps = __import__(game + '_dict')
    for action in rps.GameAction:
        if not rps.assess_game(action, move):
             return action  

# This function computes the best move for the game based on the previous game and the history
def get_prediction_agent_action(game):
    rps = __import__(game + '_dict')
    data = get_data(game)

    if len(data) > 4:
        last_game = data.tail(1)
        similar_games = data.loc[(data['agent_move'] == last_game['agent_move'].iloc[0]) & (data['rival_move'] == last_game['rival_move'].iloc[0])]
        next_indexes = list(filter(lambda y: y < len(data), list(map(lambda x: x+1 , list(similar_games.index)))))
        next_games = data.iloc[next_indexes]
        next_rival = next_games['rival_move'].value_counts().head(1).index.tolist()
        if len(next_rival) > 0:
            next_rival = next_rival[0]
            action = rps.GameAction(get_victory_action(next_rival, game))
        else:
            action = rps.GameAction(choice(range(len(rps.GameAction))))
    else:
        action = rps.GameAction(choice(range(len(rps.GameAction))))
    return action
