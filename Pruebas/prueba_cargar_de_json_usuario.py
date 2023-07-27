import json
import sys
sys.path.append(r'.\models')
from Usuario import Usuario


# lista_usuarios = Usuario.cargar_de_json("data\evento.json")
# print(lista_usuarios)
ruta = r"C:\Users\Cristian\Documents\Academia Cimmer Iber\Programacion Python\Archivos Proyecto Final\Proyecto_final_Python\Pruebas\evento.json"
ruta1 = "evento.json"
ruta2 = r"data\usuario.json"
# with open(ruta2, "r") as f:
#     data = json.load(f)
# for usuario in data:
#     del usuario["Tipo"]
#     u1 = Usuario(**usuario)
#     print(type(u1))
#     print(u1)

lista_usuarios = Usuario.cargar_de_json(ruta2)
print(type(lista_usuarios))
for usuario in lista_usuarios:
    print(usuario)
    print(type(usuario))