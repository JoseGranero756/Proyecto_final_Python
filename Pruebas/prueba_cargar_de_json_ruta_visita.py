import json
import sys
sys.path.append(r'.\models')
from RutaVisita import RutaVisita


ruta2 = r"data\RutaVisita.json"

lista = RutaVisita.cargar_de_json(ruta2)
print('Ya se cargo la lista de objetos RutaVisita en "Lista" ha sido creada para manejarla.')