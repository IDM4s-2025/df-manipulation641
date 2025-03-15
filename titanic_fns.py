import pandas as pd


tabla = pd.read_csv('data/train.csv')
def id_to_name(df, id):
    return df.loc[df["PassengerId"] == id, "Name"].iloc[0]

def nameid(df, name):
    return df.loc[df["Name"] == name, "PassengerId"].iloc[0]

nombre = "Montvila, Rev. Juozas"
passengerid = nameid(tabla, nombre)
pnombre = id_to_name(tabla, 42)
old = tabla.loc[tabla["Age"] == tabla["Age"].max()]

print(f"El ID del pasajero {nombre} es {passengerid}")
print(f"42 = {pnombre}\n")
print("El pasajero con más edad es:\n",old) 