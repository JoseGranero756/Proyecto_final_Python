import json
import sys
sys.path.append(r'.\models')
from Usuario import Usuario 

u1 = Usuario(1,"Cristian","Arias",[1,2,3])
u1_dic = u1.a_json()
print(u1_dic)
print(type(u1_dic))
#Serializa al u1_dic con dumps(dicc)
u1_json = json.dumps(u1_dic)
print(u1_json)
print(type(u1_json))
lista_dicc = []
#Serializar y guardar
for i in range(5):
    #creamos lista eventos
    l_eventos = []
    for j in range(i):
      l_eventos.append(j)
    l_eventos_json = json.dumps(l_eventos)
    #u1_dic["l_eventos"] = l_eventos_json
    #Creamos usuario i
    u1 = Usuario(i,"Nombre"+str(i), "Apellido" + str(i), l_eventos_json)
    u1_dic = u1.a_json()
    lista_dicc.append(u1_dic)
    #Cargamos el usuario
with open(r"data\evento.json","w") as Eventos:
    json.dump(lista_dicc,Eventos, indent=4)
    Eventos.write("\n")
    

