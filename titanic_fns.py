# 1. 
import pandas as pd
def get_name(Df, PassengerId):
    passenger = Df[Df["PassengerId"] == PassengerId]
    if not passenger.empty:
        return passenger["Name"].values[0]
    return "No se encontró el ID"

#2
def get_id(Df, name):
    passenger = Df[Df["Name"] == name]
    if not passenger.empty:
        return passenger["PassengerId"].values[0]
    return "No se encontró el nombre."

#7
def survival(subset: pd.Series, df:pd.DataFrame)-> float:
    return titanic[subset]['Survived'].mean()*100 if subset.any() else 0.0