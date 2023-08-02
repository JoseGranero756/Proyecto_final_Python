import json

class Review:
    def __init__(self, id_review, id_evento, id_usuario, calificacion , comentario, animo):
        self.id_review = id_review
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo #nEl profe dijo que podria ser un boton que cada que lo arpieten sume uno
    
    @classmethod
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
                "id_review" : self.id_review, 
                "id_evento" : self.id_evento, 
                "id_usuario": self.id_usuario, 
                "calificacion" : self.calificacion, 
                "comentario" : self.comentario, 
                "animo" : self.animo}
    
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            json_reviews = json.load(f)
        lista_objeto_review = []
        for json_review in json_reviews:
            del json_review["Tipo"]
            review_objeto = cls.de_json(json_review)
            lista_objeto_review.append(review_objeto)    
        return lista_objeto_review
    
    @classmethod
    def cargar_a_json(cls,archivo,lista):
        with open(archivo, "w") as f:
            json.dump(lista, f, indent=4)
        print("Guardado correctamente.")
