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

def get_survivors_over_60(df: pd.DataFrame) -> pd.DataFrame:
    """Obtiene la información de los sobrevivientes mayores de 60 años.

    Args:
        df (pd.DataFrame): Conjunto de datos

    Returns:
        pd.DataFrame: Filas de los sobrevivientes mayores de 60 años
    """
    return df[(df['Age'] > 60) & (df['Survived'] == 1)]

def count_survivors_over_60(df: pd.DataFrame) -> int:
    """Cuenta cuántas personas mayores de 60 sobrevivieron.

    Args:
        df (pd.DataFrame): Conjunto de datos

    Returns:
        int: Número de sobrevivientes mayores de 60 años
    """
    return len(get_survivors_over_60(df))

def percentage_survivors_over_60(df: pd.DataFrame) -> float:
    """Calcula el porcentaje de personas mayores de 60 que sobrevivieron.

    Args:
        df (pd.DataFrame): Conjunto de datos

    Returns:
        float: Porcentaje de sobrevivientes mayores de 60
    """
    total_over_60 = len(df[df['Age'] > 60])
    survivors = count_survivors_over_60(df)
    return (survivors / total_over_60) * 100 if total_over_60 > 0 else 0