import json

class Ubicacion:
    def __init__(self, id_ubicacion, nombre ,direccion , coordenadas):
        self.id_ubicacion = id_ubicacion 
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas #Latitud y longitud
    
        
    @classmethod
    def de_json(cls, json_dato):
        """Devuelve un ojeto de tipo de esta clase."""
        id_ubicacion = json_dato["id_ubicacion"] 
        nombre = json_dato["nombre"]
        direccion = json_dato["direccion"]
        coordenadas = json_dato["coordenadas"]
        return cls(id_ubicacion, nombre ,direccion , coordenadas)

    def a_json(self):
        """Devuelve un diccionario con la informacion del objeto."""
        return {
                "Tipo" : "Ubicación" , 
                "id_ubicacion" : self.id_ubicacion, 
                "nombre" : self.nombre, 
                "direccion" : self.direccion, 
                "coordenadas" : self.coordenadas
                #Si queremos que esto vaya a json calculo que queremos que esto sea ya convertido a texto 
                }
    
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            json_ubicacion = json.load(f)
        lista_objeto_ubicacion = []
        for json_ubicacion in json_ubicacion:
            del json_ubicacion["Tipo"]
            ubicacion_objeto = cls.de_json(json_ubicacion)
            lista_objeto_ubicacion.append(ubicacion_objeto)    
        return lista_objeto_ubicacion

