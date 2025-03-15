# titanic_fns.py
import pandas as pd

# Punto 1: Obtener nombre por ID
def get_name(df: pd.DataFrame, passenger_id: int) -> str:
    
    """Devuelve el nombre del pasajero dado su ID."""
    passenger = df[df["PassengerId"] == passenger_id]
    return passenger["Name"].values[0] if not passenger.empty else "ID no encontrado" 

# Punto 2: Obtener ID por nombre
def get_id(df: pd.DataFrame, name: str) -> int:
    """Devuelve el ID del pasajero dado su nombre."""
    passenger = df[df["Name"] == name]
    return passenger["PassengerId"].values[0] if not passenger.empty else "Nombre no encontrado"

# Puntos 7-9: Funciones para análisis de sobrevivientes
def survivors_over_60(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra sobrevivientes mayores de 60 años."""
    return df[(df["Age"] > 60) & (df["Survived"] == 1)]

def survival_percentage(df: pd.DataFrame) -> float:
    """Calcula el porcentaje de sobrevivientes mayores de 60."""
    survivors = survivors_over_60(df)
    total_over_60 = len(df[df["Age"] > 60])
    return (len(survivors) / total_over_60 * 100) if total_over_60 > 0 else 0
