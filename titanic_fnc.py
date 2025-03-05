import pandas as pd


def id_to_name(df: pd.DataFrame, id: int) -> str:
    """Regresa el nombre del pasajero dado su id.

    Args:
        df (pd.DataFrame): El conjunto de datos
        id (int): ID del pasajero

    Returns:
        str: Nombre del pasajero
    """
    passenger = df[df.PassengerId == id].Name
    return passenger[id-1]



def name_to_id(df: pd.DataFrame, name: str) -> int:
    """Regresa el ID del pasajero dado su nombre.

    Args:
        df (pd.DataFrame): El conjunto de datos
        name (str): Nombre del pasajero

    Returns:
        int: ID del pasajero
    """
    passenger = df[df.Name == name].PassengerId
    return int(passenger.iloc[0])




def message_name_to_id(df: pd.DataFrame, name: str) -> int:
    """Regresa un mensaje del ID del pasajero dado su nombre.

    Args:
        df (pd.DataFrame): El conjunto de datos
        name (str): Nombre del pasajero

    Returns:
        int: Mensaje con el ID del pasajero
    """
    passenger = df[df.Name == name].PassengerId
    return print(f"The ID of passenger {name} is: {int(passenger.iloc[0])}") 


def message_id_to_name(df: pd.DataFrame, id: int) -> str:
    """Regresa un mensaje con el nombre del pasajero dado su id.

    Args:
        df (pd.DataFrame): El conjunto de datos
        id (int): ID del pasajero

    Returns:
        str: Mensaje con el nombre del pasajero
    """
    passenger = df[df.PassengerId == id].Name
    return print(f"The passenger with ID {id} is {passenger[id-1]}")
    

def print_all_info(df: pd.DataFrame) -> pd.DataFrame:
    """Regresa toda la información del valor máximo.

    Args:
        df (pd.DataFrame): El conjunto de datos

    Returns:
        pd.DataFrame: Toda la información del pasajero
    """
    passenger = df[df.Age == df.Age.max()]
    return print(passenger)