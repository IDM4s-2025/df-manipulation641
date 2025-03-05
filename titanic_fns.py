import pandas as pd

# Ejercicio 1

def name_to_id(df: pd.DataFrame, name: str) -> int:
    id: int = df[df.Name == name].PassengerId.iat[0].item()
    return id

# Ejercicio 2
def id_to_name(df: pd.DataFrame, id: int) -> str:
    name: str = df[df.PassengerId == id]['Name'].iat[0]
    return name