import pandas as pd
datos = pd.read_csv("Data/train.csv")
def get_name(datos:pd.DataFrame, int: id) -> str:
    """
    Recibe un id y devuelve el nombre asociado
    Args:
        id (int): id del pasagero

    Returns:
        str: nombre del pasajero
    """

    nombre = datos.loc[datos["PassengerId"] == id, "Name"].values    
    return nombre



def get_id(datos:pd.DataFrame,nombre: str)-> int:
    """
    Recibe un nombre y devuelve el id asociado
    Args:
        nombre (str): nombre del pasajero

    Returns:
        int: id asociado al nombre del pasajero
    """
    id = datos.loc[datos["Name"] == nombre,"PassengerId"].values
    return id

id = get_id(datos,"Montvila, Rev. Juozas")
print("The ID of passenger Montvila, Rev.Juozas is", id)
name = get_name(datos,42)
print("The passenger with ID 42 is ",name)