def id_to_name(df:pd.DataFrame,id: int) -> str: #name of argument:pd.DataFrame
    passenger_name = df[df.PassengerId == id].Name
    return passenger_name[id-1]

def name_to_id(df:pd.DataFrame,name: str)-> int:
    passenger_id = df[df.Name == name].PassengerId
    return passenger_id.iloc[0]

def messages_id(df:pd.DataFrame, name: str)-> int:
    passenger_id = df[df.Name == name].PassengerId
    return print(f"The ID pf passenger of {name} is: {passenger_id.iloc[0]}")

def messages_name(df:pd.DataFrame, id:int)-> str:
    passenger_name = df[df.PassengerId == id].Name
    return print(f"'The passenger with ID {id} is {passenger_name[id-1]}")

def print_info(df:pd.DataFrame)->pd.DataFrame:
    passenger_info = df[df.Age == df.Age.max()]
    return print(passenger_info)