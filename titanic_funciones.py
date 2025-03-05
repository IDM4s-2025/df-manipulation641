import pandas as pd

def id_to_name(df: pd.DataFrame, id: int) -> str:
    """Regresa el nombre del pasajero con el id dado

    Args:
        df (pd.DataFrame): El conjunto de datos de titanic
        id (int): El id del pasajero

    Returns:
        str:    El nombre del pasajero
    """
    nombre = df.loc[df['PassengerId'] == id]['Name']
    return str(nombre.values[0])

def name_to_id(df: pd.DataFrame, name: str) -> int:
    """Regresa el id del pasajero con el nombre dado

    Args:
        df (pd.DataFrame): El conjunto de datos de titanic
        name (str): El nombre del pasajero

    Returns:
        int:    El id del pasajero
    """
    id = df.loc[df['Name'] == name]['PassengerId']
    return int(id.values[0])