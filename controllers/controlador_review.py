import sys
sys.path.append(r'.\models')
from Review import Review

class ControladorReview:
    def __init__(self,app,modelo_evento,modelo_review):
        self.app = app
        self.modelo_evento = modelo_evento
        self.modelo_review = modelo_review
    
    def guardar(self, id_review, id_evento, id_usuario, calificacion , comentario, animo):
        review = Review(id_review, id_evento, id_usuario, calificacion , comentario, animo)
        self.modelo_review.append(review)
        lista_Aux = []
        for r in self.modelo_review: #Transforma cada objeto review a_json
            lista_Aux.append(r.a_json())
        self.modelo_review = lista_Aux
        Review.cargar_a_json(r"data\Review.json", self.modelo_review)
        print("Review creada. Esperando ser guardada.")

    def volver_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)        
    

        
        