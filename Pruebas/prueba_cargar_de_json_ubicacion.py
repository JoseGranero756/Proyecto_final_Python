import json
import sys
sys.path.append(r'.\models')
from Ubicación import Ubicacion


ruta2 = r"data\Ubicacion.json"

lista = Ubicacion.cargar_de_json(ruta2)
print(type(lista))
for elemento in lista:
    print(elemento)
    print(type(elemento))
print("Ya se cargo la lista de objetos Ubicación ha sido creada para manejarla. ")

