import pandas as pd
df = pd.read_csv('data/train.csv')
print(df.head())

def get_passenger_name(passenger_id):
    """Regresa el nombre del pasajero dado su id. Si no existe el pasajero, regresa None.

Args: 
    passenger_id (int): El id del pasajero.

Returns:
    str: El nombre del pasajero o None si no existe.

"""
    passenger = df.loc[df['PassengerId'] == passenger_id]
    if not passenger.empty:
        return passenger.iloc[0]['Name']
    else:
        return None
    
    
def get_passenger_id(name):
    passenger = df.loc[df['Name'] == name]
    if not passenger.empty:
        return passenger.iloc[0]['PassengerId']
    else:
        return None
    
def survival_rate(subset):
    """
    Returns the percentage of people that survived from a subset given as a boolean Pandas series.

    Args:
    subset (pd.Series): A boolean series indicating the subset of the dataframe.

    Returns:
    float: The percentage of people that survived in the subset.
    """
    subset_df = df[subset]
    if len(subset_df) == 0:
        return 0.0
    survival_rate = subset_df['Survived'].mean() * 100
    return survival_rate

    
    