import json
import datetime
from PIL import Image
import random
import sys
sys.path.append(r'.\models')
from Evento import Evento 

#Serializar y guardar
lista_dicc = []
for i in range(5):
    hora_aleatoria_inicio = datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    hora_inicio = hora_aleatoria_inicio.isoformat()
    hora_aleatoria_fin = datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)) 
    hora_fin = hora_aleatoria_fin.isoformat()
    #Creamos evento i
    e1 = Evento(
                i,
                "Nombre"+str(i), 
                "Artista" + str(i),
                "Genero" + str(random.randint(1, 5)),
                str(random.randint(1, 10)),#id_ubicacion
                hora_inicio,
                hora_fin,
                "Descripcion"+str(i),
                "Ruta\imagen" + str(i))
    
    e1_dic = e1.a_json()
    lista_dicc.append(e1_dic)
    #Cargamos el usuario
with open(r"data\evento.json","w") as Usuario:
    json.dump(lista_dicc,Usuario, indent=4)
    Usuario.write("\n")
    

