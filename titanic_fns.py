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
# Punto 7: Filtrar sobrevivientes mayores de 60 años
def survivors_over_60(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra sobrevivientes mayores de 60 años."""
    return df[(df["Age"] > 60) & (df["Survived"] == 1)]

# Punto 8: Calcular el número de sobrevivientes mayores de 60
def survivors_over_60_count(df: pd.DataFrame) -> int:
    """Devuelve el número de sobrevivientes mayores de 60 años."""
    survivors = survivors_over_60(df)  # Usa la función del punto 7
    return len(survivors)

# Punto 9: Calcular el porcentaje de sobrevivientes mayores de 60
def survival_percentage(df: pd.DataFrame) -> float:
    """Calcula el porcentaje de sobrevivientes mayores de 60."""
    survivors = survivors_over_60(df)  # Usa la función del punto 7
    total_over_60 = len(df[df["Age"] > 60])  # Total de pasajeros mayores de 60
    return (len(survivors) / total_over_60 * 100) if total_over_60 > 0 else 0
