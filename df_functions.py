import pandas as pd
import numpy as np


def id_2_name(df: pd.DataFrame, id: int) -> str:
    """
    Takes a PassengerId as input and returns the name of the corresponding passenger.
    The function retrieves the Name field from the Titanic DataFrame.
    """
    return df[df.PassengerId == id].Name.values[0]


def name_2_id(df: pd.DataFrame, name: str) -> int:
    """
    Takes a Passenger name as input and returns the id of the corresponding passenger.
    The function retrieves the id field from the Titanic DataFrame.
    """
    return df[df.Name == name].PassengerId.values[0]
