import pandas as pd

def id_to_name(df: pd.DataFrame, id: int) -> str:
    """Regresa el nombre del pasajero dado su ID

    Args:
        df (pd.DataFrame): el conjunto de datos
        id (int): el id del pasajero

    Returns:
        str: el nombre del pasajero
    """
    name = df.loc[df["PassengerId"] == id, "Name"]
    return name.iloc[0]

def name_to_id(df: pd.DataFrame, name: str) -> int:
    """Regresa el ID del pasajero dado su nombre

    Args:
        df (pd.DataFrame): el conjunto de datos
        name (str): el nombre del pasajero

    Returns:
        int: el ID del pasajero
    """
    passenger_id = df.loc[df["Name"] == name, "PassengerId"]
    return passenger_id.iloc[0]

def oldest_passenger(df: pd.DataFrame) -> pd.Series:
    return df.loc[df["Age"].idxmax()]

