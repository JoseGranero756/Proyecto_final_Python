import json
import datetime
import random
import sys
sys.path.append(r'.\models')
from RutaVisita import RutaVisita 

#Serializar y guardar
lista_dicc = []
for i in range(5):
    l_destinos = []
    for j in range(2):
        l_destinos.append(random.randint(1, 4))
    #Creamos Review i
    rv1 = RutaVisita(
        i, 
        "Ruta "+str(i), 
        l_destinos
        )
    rv1_dic = rv1.a_json()
    lista_dicc.append(rv1_dic)
    #Cargamos el ruta_visita
with open(r"data\RutaVisita.json","w") as RutaVisita:
    json.dump(lista_dicc,RutaVisita, indent=4)
    RutaVisita.write("\n")
