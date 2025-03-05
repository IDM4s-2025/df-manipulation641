def get_passenger_name(passenger_id, df):
    result = df.loc[df['PassengerId'] == passenger_id, 'Name']
    return result.values[0] if not result.empty else None

def get_passenger_id(name, df):
    result = df.loc[df['Name'] == name, 'PassengerId']
    return result.values[0] if not result.empty else None