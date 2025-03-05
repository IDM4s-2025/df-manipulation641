import pandas as pd
def name_to_id(df: pd.DataFrame, name: str) -> int:
    id: int = df[df.Name == name].PassengerId.iat[0].item()
    return id

def id_to_name(df: pd.DataFrame, id: int) -> str:
    name: str = df[df.PassengerId == id].Name.iat[0]
    return name