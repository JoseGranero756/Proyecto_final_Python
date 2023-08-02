class ControladorInfo:
    def __init__(self,app):
        self.app = app
    
    def hacer_review(self,evento):
        self.app.vista_review.hacer_review(evento)
        self.app.cambiar_frame(self.app.vista_review)
        
    
    def volver_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
        
    
    
    