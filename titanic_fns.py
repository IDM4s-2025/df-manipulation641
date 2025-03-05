import pandas as pd



train = pd.read_csv('data/train.csv')

train



def get_passenger(df:pd.DataFrame, passengerId:int):
    """Regrese el nombre del pasajero segun su id

    Args:
        df (pd.DataFrame): Conjunto de datos
        passengerId (int): Id del pasajero

    Returns:
        str: El nombre del pasajero
    """
    return df.Name[df.PassengerId == passengerId].values[0]

def get_passengerId(df:pd.DataFrame, passenger:str):
    """Regrese el id del pasajero segun su nombre

    Args:
        df (pd.DataFrame): Conjunto de datos
        passenger (str): Nombre del pasajero

    Returns:
        int: Id del pasajero
    """
    return df.PassengerId[df.Name ==passenger].values[0]

