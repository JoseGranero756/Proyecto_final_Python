import json
objetos_json = []
with open("Eventos.json","r") as Eventos:
    for linea in Eventos:
        #primer_usuario = Eventos.readline().strip()
        objeto = json.loads(linea.strip()) #--> dicc
        objetos_json.append(objeto)

for objeto in objetos_json:
    print(objeto)
    #print(type(objeto)) 
    print(objeto['Historial de eventos'])


# print(type (primer_usuario))
# print(type(primer_objeto))
# print(primer_usuario)
# print(primer_objeto)
# print(primer_objeto['Historial de eventos'])
# print(type(list(primer_objeto['Historial de eventos'])))