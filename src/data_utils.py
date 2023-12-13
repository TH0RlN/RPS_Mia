import pandas as pd
import pathlib as p

#History route
ROUTE = '../media/history'
TAIL = '.csv'

# Retrieves the data from the csv
def get_data(name):
    file = p.Path(ROUTE + '/' + name + TAIL)
    route = p.Path(ROUTE)

    if not route.is_dir():
         from os import mkdir
         mkdir(ROUTE)

    if file.is_file():
        return pd.read_csv(ROUTE + '/' + name + TAIL)
    else:
        return pd.DataFrame(columns=('agent_move', 'rival_move', 'result'))

# Stores last move on a csv
def store_data(agent_move, rival_move, result, name):
    data = get_data(name)
    data.loc[len(data)] = list((agent_move, rival_move, result))
    data.to_csv(ROUTE + '/' + name + TAIL, index=False)