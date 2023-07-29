class ControladorInfo:
    def __init__(self,app):
        self.app = app
    
    def regresar_eventos(self):
        self.app.cambiar_frame(self.app.vista_eventos)
    
    def regresar_eventos_asistidos(self):
        self.app.cambiar_frame(self.app.vista_eventos_asistidos)
    