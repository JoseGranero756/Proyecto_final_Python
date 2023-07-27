import json
import datetime
class Evento:
    def __init__(
            self,
            id_evento, #modifique nombre id para mas claridad.
            nombre,
            artista,
            genero,
            id_ubicacion,
            hora_inicio,
            hora_fin,
            descripcion,
            imagen):
        
        self.id_evento = id_evento
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen
        
        
    @classmethod
    def de_json(cls, json_dato):
        """Devuelve un ojeto de tipo de esta clase."""
        id_evento = json_dato["id_evento"]
        nombre = json_dato["nombre"]
        artista = json_dato["artista"]
        genero = json_dato["genero"]
        id_ubicacion = json_dato["id_ubicacion"]
        hora_inicio = json_dato["hora_inicio"]
        hora_fin = json_dato["hora_fin"]
        descripcion = json_dato["descripcion"]
        imagen = json_dato["imagen"]
        return cls(
            id_evento, 
            nombre,
            artista,
            genero,
            id_ubicacion,
            hora_inicio,
            hora_fin,
            descripcion,
            imagen
        )
    
    def a_json(self):
        """Devuelve un diccionario con la informacion del objeto."""
        return { 
                "Tipo" : "Evento", 
                "id_evento" : self.id_evento, 
                "nombre" : self.nombre, 
                "artista" : self.artista, 
                "genero" : self.genero, 
                "id_ubicacion" : self.id_ubicacion, 
                "hora_inicio" : self.hora_inicio, 
                "hora_fin" : self.hora_fin, 
                "descripcion" : self.descripcion, 
                "imagen" : self.imagen
                }
    
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            json_eventos = json.load(f)
        lista_objeto_eventos = []
        for json_evento in json_eventos:
            del json_evento["Tipo"]
            evento_objeto = cls.de_json(json_evento)
            lista_objeto_eventos.append(evento_objeto)    
        return lista_objeto_eventos  