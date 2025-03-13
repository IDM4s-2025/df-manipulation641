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


def survival_rates_by_gender_and_age(df: pd.DataFrame):
    """Calcula la tasa de supervivencia para mujeres, hombres y niños (menores de 18)."""
    women_survival_rate = df[df["Sex"] == "female"]["Survived"].mean() * 100
    men_survival_rate = df[df["Sex"] == "male"]["Survived"].mean() * 100
    children_survival_rate = df[df["Age"] < 18]["Survived"].mean() * 100

    return {
        "Women Survival Rate": women_survival_rate,
        "Men Survival Rate": men_survival_rate,
        "Children Survival Rate": children_survival_rate
    }



def survival_rate_subset(df: pd.DataFrame, subset: pd.Series) -> float:
    """Calcula el porcentaje de personas que sobrevivieron dentro de un subconjunto dado como una serie booleana."""
    subset_df = df[subset]  
    if subset_df.shape[0] == 0:  
        return 0
    survival_rate = subset_df["Survived"].mean() * 100  
    return survival_rate


def median_age(df: pd.DataFrame) -> float:
    """Calcula la edad mediana de los pasajeros."""
    return df["Age"].median()


def passengers_per_port(df: pd.DataFrame) -> pd.Series:
    """Cuenta cuántos pasajeros embarcaron en cada puerto."""
    return df["Embarked"].value_counts()

def survival_rate_by_fare(df: pd.DataFrame, threshold: float) -> tuple:
    """Calcula la tasa de supervivencia para pasajeros que pagaron más o menos que el umbral dado."""
    high_fare = df["Fare"] > threshold
    low_fare = df["Fare"] <= threshold

    high_fare_survival = df[high_fare]["Survived"].mean() * 100 if df[high_fare].shape[0] > 0 else 0
    low_fare_survival = df[low_fare]["Survived"].mean() * 100 if df[low_fare].shape[0] > 0 else 0

    return high_fare_survival, low_fare_survival


def survival_rate_by_port(df: pd.DataFrame) -> pd.Series:
    """Calcula la tasa de supervivencia por puerto de embarque."""
    return df.groupby("Embarked")["Survived"].mean() * 100
