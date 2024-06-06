import csv
import json

# Creo un archivo CSV

texto = [['Nombre', 'Edad', 'Ciudad'],
        ['Maria', 30, 'Madrid'],
        ['Silvia', 25, 'Barcelona']]

with open('texto.csv', 'w', newline='') as fichero:
    fichero = csv.writer(fichero)
    fichero.writerows(texto)

# Una vez creado el archivo CSV pasamos a transformarlo al formato json

datos = []

# Abro y leo el archivo en formato csv y añado los datos a una lista
with open('texto.csv', 'r', newline='') as fichero:
    fichero = csv.DictReader(fichero)
    for linea in fichero:
        datos.append(linea)

# Creo un archivo en formato json y añado la lista creada con los datos provenientes del archivo csv
with open('texto.json', 'a') as fichero:
    json.dump(datos, fichero, indent=4)

