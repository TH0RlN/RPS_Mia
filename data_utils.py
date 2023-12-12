import pandas as pd
import pathlib as p

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