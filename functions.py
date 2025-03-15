import pandas as pd

def id_to_name(df:pd.DataFrame, id:int)->str:
    """_summary_

    Args:
        df (pd.DataFrame): Data Frame
        id (int): Id of the passenger

    Returns:
        str: Name of the passenger
    """
    passenger = df[df.PassengerId == id].Name
    res = passenger[id-1]
    return res

def name_to_id(df : pd.DataFrame , name:str)-> int:
    """_summary_

    Args:
        df (pd.DataFrame): Data frame
        name (str): Name of the passenger

    Returns:
        int: Id of the passenger
    """
    passenger = df[df.Name == name].PassengerId
    return print(int(passenger.iloc[0]))

def message_name_to_id(df: pd.DataFrame,name: str)-> int:
    """_summary_

    Args:
        df (pd.DataFrame): Data frame
        name (str): Name of the passenger

    Returns:
        int: Id
    """
    passenger = df[df.Name == name].PassengerId
    print(f"The ID of passenger{name} is: {int(passenger.iloc[0])}")
    return 0

def message_id_to_name(df: pd.DataFrame,id: int)-> str:
    """_summary_

    Args:
        df (pd.DataFrame): Data frame
        id (int): PassengerId

    Returns:
        str: Returns name
    """
    passenger = df[df.PassengerId == id].Name
    print(f"The passenger with ID {id} is: {passenger[id-1]}")
    return 0

def print_all_info(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): Data frame

    Returns:
        pd.DataFrame: Is a void method
    """
    passenger = df[df.Age == df.Age.max()]
    print(passenger)
    return 0

def percentage(subset:pd.Series , survived:pd.Series)-> float:
    """_summary_

    Args:
        subset (pd.Series): Series
        survived (pd.Series): Series

    Returns:
        float: Percentage
    """
    res = float(percentage)
    return res
