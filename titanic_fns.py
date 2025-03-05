import pandas as pd
datos = pd.read_csv("Data/train.csv")
def get_name(id: int) -> str:
    """
    Recibe un id y devuelve el nombre asociado
    Args:
        id (int): id del pasagero

    Returns:
        str: nombre del pasajero
    """

    nombre = datos.loc[datos["PassengerId"] == id, "Name"].values    
    return nombre



def get_id(nombre: str)-> int:
    """
    Recibe un nombre y devuelve el id asociado
    Args:
        nombre (str): nombre del pasajero

    Returns:
        int: id asociado al nombre del pasajero
    """
    id = datos.loc[datos["Name"] == nombre,"PassengerId"].values
    return id