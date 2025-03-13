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

def survival_rate(subset: pd.Series, df: pd.DataFrame) -> float:
    """
    Returns the percentage of people that survived from a given subset.
    
    Parameters:
        subset (pd.Series): A boolean Series indicating the subset of passengers.
        df (pd.DataFrame): The Titanic dataset.

    Returns:
        float: Percentage of survivors in the subset.
    """
    passengers = df[subset]

    totalPassengers = passengers.shape[0]

    passengersSurvived = passengers["Survived"].sum()

    return (passengersSurvived / totalPassengers) * 100

