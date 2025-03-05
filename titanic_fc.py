#1
def get_passenger_name(passenger_id):
    """
    Returns the name of a passenger given their PassengerId.
    

    """
    row = titanic.loc[titanic['PassengerId'] == passenger_id, 'Name']
    if not row.empty:
        return row.values[0]
    else:
        return "Passenger ID not found"

passenger_id = int(input("Enter PassengerID")) # Change this value to test different IDs
print(get_passenger_name(passenger_id))

#2
def get_passenger_id(name):
    """
    Returns the PassengerId of a passenger given their Name.
    """
    row = titanic.loc[titanic['Name'].str.lower() == name.lower(), 'PassengerId']
    if not row.empty:
        return row.values[0]
    else:
        return "Passenger Name not found"

# Ask the user for a Name
passenger_name = input("Enter Passenger Name: ").strip()
print("Passenger ID:", get_passenger_id(passenger_name))

#3
def get_passenger_id(name):
    """
    Returns the PassengerId of a passenger given their Name.
    """
    row = titanic.loc[titanic['Name'] == name, 'PassengerId']
    if not row.empty:
        return row.values[0]
    else:
        return None

# Passenger name
passenger_name = "Montvila, Rev. Juozas"

# Get the Passenger ID
passenger_id = get_passenger_id(passenger_name)

# Print the message
if passenger_id:
    print(f'The ID of passenger {passenger_name} is {passenger_id}')
else:
    print(f'Passenger {passenger_name} not found')

#4
def get_passenger_name(passenger_id):
    """
    Returns the name of a passenger given their PassengerId.
    """
    row = titanic.loc[titanic['PassengerId'] == passenger_id, 'Name']
    if not row.empty:
        return row.values[0]
    else:
        return None

# Get the name of the passenger with ID 42
passenger_id = 42
name = get_passenger_name(passenger_id)

# Print the message
if name:
    print(f'The passenger with ID {passenger_id} is {name}')
else:
    print(f'Passenger with ID {passenger_id} not found')