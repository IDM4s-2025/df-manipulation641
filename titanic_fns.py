import pandas as pd

def Name_byId(df: pd.DataFrame, id: int) -> str:
    """Regresa el nombre del pasajero dado su id"""
    name = df.loc[df["PassengerId"] == id, "Name"]
    return name.iloc[0] if not name.empty else "Passenger not found"

def Id_byName(df: pd.DataFrame, name: str) -> int:
    """Regresa el id del pasajero dado su nombre"""
    id = df.loc[df["Name"] == name, "PassengerId"]
    return id.iloc[0] if not id.empty else -1

def get_oldest_passenger(df: pd.DataFrame) -> pd.Series:
    """Obtiene toda la información del pasajero más viejo"""
    return df.loc[df["Age"].idxmax()]

def create_subset(df: pd.DataFrame, filename: str):
    """Crea y guarda un subconjunto de los datos con las primeras 100 filas"""
    subset = df[["Pclass", "Fare", "Embarked"]].head(100)
    subset.to_csv(filename, index=False)

def get_survivors_over_60(df: pd.DataFrame) -> pd.DataFrame:
    """Obtiene los sobrevivientes mayores de 60 años"""
    return df[(df["Age"] > 60) & (df["Survived"] == 1)]

def count_survivors_over_60(df: pd.DataFrame) -> int:
    """Cuenta cuántas personas mayores de 60 sobrevivieron"""
    return get_survivors_over_60(df).shape[0]

def percentage_survivors_over_60(df: pd.DataFrame) -> float:
    """Calcula el porcentaje de personas mayores de 60 que sobrevivieron"""
    total_over_60 = df[df["Age"] > 60].shape[0]
    num_survivors = count_survivors_over_60(df)
    return (num_survivors / total_over_60) * 100 if total_over_60 > 0 else 0