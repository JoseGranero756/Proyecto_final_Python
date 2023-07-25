import json

class Review:
    def __init__(self, id_review, id_evento, id_usuario, calificacion , comentario, animo):
        self.id_review = id_review
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def de_json(cls, json_dato):
        """Devuelve un ojeto de tipo de esta clase."""
        id_review = json_dato["id_review"]
        id_evento = json_dato["id_evento"]
        id_usuario = json_dato["id_usuario"]
        calificacion = json_dato["calificacion"]
        comentario = json_dato["comentario"]
        animo = json_dato["animo"]
        return cls(id_review, id_evento, id_usuario, calificacion , comentario, animo)     
        
    def a_json(self):
        """Devuelve un diccionario con la informacion del objeto."""
        return {"Tipo" : "Review", 
                "id" : self.id, 
                "id evento" : self.id_evento, 
                "id usuario": self.id_usuario, 
                "Calificación" : self.calificacion, 
                "Comentario" : self.comentario, 
                "Animo" : self.animo}