import json

class RutaVisita:
    def __init__(self,id_ruta_visita,nombre,destinos): 
        self.id_ruta_visita = id_ruta_visita
        self.nombre = nombre
        self.destinos = destinos #Lista de enteros con id_ubicacion o id_Eventos dependiendo de como se implemente

    def agregar_destino(self,destino):
        self.destinos.append(destino)
    
    @classmethod    
    def de_json(cls, json_dato):
        """Devuelve un ojeto de tipo de esta clase."""
        id_ruta_visita = json_dato["id_ruta_visita"]
        nombre = json_dato["nombre"]
        destinos = json_dato["destinos"]
        return cls(id_ruta_visita,nombre,destinos)

    def a_json(self):
        """Devuelve un diccionario con la informacion del objeto."""
        return {"Tipo" : "RutaVisita", 
                "id_ruta_visita" : self.id_ruta_visita, 
                "nombre" : self.nombre, 
                "destinos" : self.destinos}
    
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            json_ruta_visitas = json.load(f)
        lista_objeto_rv = []
        for json_rv in json_ruta_visitas:
            del json_rv["Tipo"]
            usuario_objeto = cls.de_json(json_rv)
            lista_objeto_rv.append(usuario_objeto)    
        return lista_objeto_rv    