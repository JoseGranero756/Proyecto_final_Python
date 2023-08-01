class ControladorInfo:
    def __init__(self,app):
        self.app = app
    
    def volver_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
    
    
    