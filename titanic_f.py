import pandas as pd

#1
def id_to_name(df: pd.DataFrame, id: int) -> str:
    passenger_name = df[df.PassengerId == id].Name
    return passenger_name[id-1]


#2
def name_to_id(df: pd.DataFrame, name: str) -> int:
    passenger_id = df[df.Name == name].PassengerId
    return passenger_id.iloc[0]

# 11
def survival_rate(subset: pd.Series, df: pd.DataFrame) -> float:
    subset_df = df[subset]
    return subset_df["Survived"].mean() * 100

 

