import pandas as pd

def conocer_nombre(df: pd.DataFrame, id:int)->str:
    """Te da el nombre dado un dataframe y el PassengerID

    Args:
        df (pd.DataFrame): Un dataframe
        int (id): EL ID del pasajero

    Returns:
        str: Regresa el nombre del pasjero
    """
    id=id-1
    nombre=df.iloc[id]["Name"]
    return nombre
def conocer_id(df: pd.DataFrame, nombre:str)->int:
    """Te da el PassengerID dado un dtaframe y el nombre

    Args:
        df (pd.DataFrame): Un dataframe
        nombre (str): El nombre del pasajero
    Returns:
        int: El Passengers ID
    """
    id=df[df["Name"]==nombre].values[0][0]
    return id
def conocer_porcentaje(df: pd.DataFrame)->int:
    """Te da el porcentaje de sobrevivientes del subset

    Args:
        df (pd.DataFrame): Un data frame

    Returns:
        int: El porceteaje de supervivieentes
    """
    porcentaje=len(df[df["Survived"]==1])*100/len(df)
    return porcentaje