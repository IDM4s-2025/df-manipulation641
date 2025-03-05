
import pandas as pd
# Ejercicio 1
def id_to_name(df: pd.DataFrame, id: int) -> str:
    name = df.loc[id, ['Name']]
    return name

#Ejercicio 2
def name_a_id(df: pd.DataFrame, name: str) -> int:
    id = df[df['Name'] == name].index[0]
    return id

def name_to_id(df: pd.DataFrame, name: str) -> int:
    ids = df[df['Name'] == name].index
    return ids[0]