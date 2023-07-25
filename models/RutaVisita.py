import json

class RutaVisita:
    def __init__(self,id_ruta_visita,nombre,destinos): #No entiendo que hace destino pero creo que deberia empezar en [] si lo vamos a ir agregando.
        self.id_ruta_visita = id_ruta_visita
        self.nombre = nombre
        self.destinos = destinos

    def agregar_destino(self,destino):
        self.destinos.append(destino)
        
    def de_json(cls, json_dato):
        """Devuelve un ojeto de tipo de esta clase."""
        id_ruta_visita = json_dato[id_ruta_visita]
        nombre = json_dato[nombre]
        destinos = json_dato[destinos]
        return cls(id_ruta_visita,nombre,destinos)


    def a_json(self):
        """Devuelve un diccionario con la informacion del objeto."""
        return {"Tipo" : "RutaVisita", 
                "id" : self.id, 
                "Nombre" : self.nombre, 
                "Destinos" : self.destinos}