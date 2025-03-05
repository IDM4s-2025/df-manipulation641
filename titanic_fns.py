import pandas as pd

def get_Passenger_name(df: pd.DataFrame, Id: int) -> str:
    """Regresa el nombre del pasajero con el Id dado

    Args:
        df (pd.DataFrame): Conjunto de datos
        Id (int): Id del pasajero

    Returns:
        str: Nombre del pasajero
    """
    return df.loc[df['PassengerId'] == Id]["Name"].values[0]

def get_Passenger_ID(df: pd.DataFrame, name: int) -> str:
    """Regresa el numero de id de un pasajero recibiendo su nombre

    Args:
        df (pd.DataFrame): El conjunto de datos
        name (int): Nombre del pasajero

    Returns:
        str: Numero de id
    """
    return int(df.loc[df['Name'] == name]["PassengerId"].values[0])