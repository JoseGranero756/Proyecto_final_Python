import json
#from models.Proyecto import Usuario
import sys
sys.path.append(r'.\models')
from Usuario import Usuario 
objetos_json = []
with open("evento.json","r") as Eventos:
    for linea in Eventos:
        #primer_usuario = Eventos.readline().strip()
        objeto = json.loads(linea.strip()) #--> dicc
        objetos_json.append(objeto)

l_usuarios = []
for objeto in objetos_json:
    
    #print(type(objeto))
    # print(objeto['Historial de eventos'])
    del objeto["tipo"]
    #print(objeto)
    u = Usuario.de_json(objeto)
    l_usuarios.append(u)

for usuario in l_usuarios:
    print(usuario)
    print(type(usuario))



# print(type (primer_usuario))
# print(type(primer_objeto))
# print(primer_usuario)
# print(primer_objeto)
# print(primer_objeto['Historial de eventos'])
# print(type(list(primer_objeto['Historial de eventos'])))