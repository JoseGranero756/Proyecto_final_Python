class ControladorEventos:
    def __init__(self,app,modelo_evento):
        self.app = app
        self.modelo_evento = modelo_evento
        
    def obtener_eventos(self):
        return self.modelo_evento
    
    def seleccionar_evento(self):
        """
        obtiene el indice del evento seleccionado y llama a la vista de
        información para mostrar la informacion del evento
        """
        indice = self.app.vista_
        
        