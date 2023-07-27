import json
import sys
sys.path.append(r'.\models')
from Evento import Evento


ruta2 = r"data\evento.json"

lista = Evento.cargar_de_json(ruta2)
print(type(lista))
# for elemento in lista:
    # print(elemento)
    # print(type(elemento))
print("Ya se cargo la lista de objetos Eventos ha sido creada para manejarla. ")
