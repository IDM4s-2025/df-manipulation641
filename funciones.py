import pandas as pd
import numpy as np

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

def porcentaje_sobrevivir(df:pd.DataFrame, nombre_columna:str):
    """Te da el porcentaje de personas que sobreviven en un df

    Args:
        df (pd.DataFrame): Conjunto de datos
        nombre_columna (str): Nombre de la columna binaria

    Returns:
        str: String que calcula el porcentaje de supervivientes y lo imprime
    """
    return f'{df[df[nombre_columna]==1].shape[0] / df.shape[0] * 100} %'
