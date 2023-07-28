import json
import sys
sys.path.append(r'.\models')
from Review import Review


ruta2 = r"data\Review.json"

lista = Review.cargar_de_json(ruta2)
print('Ya se cargo la lista de objetos Reviews en "Lista" ha sido creada para manejarla.')