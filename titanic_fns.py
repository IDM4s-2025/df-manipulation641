import pandas as pd

def percentage_survivors_function(df: pd.DataFrame) -> float:
    total_survivors = df[df['Survived'] == 1].shape[0]
    return (total_survivors / df.shape[0]) * 100
'''regresa el porcentaje de sobrevivientes en el dataframe dado.

Args:
    df: pd.DataFrame, dataframe de los pasajeros del Titanic.

Returns:
    float: porcentaje de sobrevivientes.
'''
def get_name_by_id(df: pd.DataFrame, passenger_id:int) -> str:
    return df.loc[df['PassengerId'] == passenger_id, 'Name'].values[0]
'''regresa el nombre del pasajero con el id dado.

Args:
    df: pd.DataFrame, dataframe de los pasajeros del Titanic.
    passenger_id: int, id del pasajero.
    
Returns:
    str: nombre del pasajero.
'''

def get_id_by_name(df: pd.DataFrame, name:str) -> int:
    return df.loc[df['Name'] == name, 'PassengerId'].values[0]
'''regresa el id del pasajero con el nombre dado.

Args:
    df: pd.DataFrame, dataframe de los pasajeros del Titanic.
    name: str, nombre del pasajero.
    
Returns:
    int: id del pasajero.
'''