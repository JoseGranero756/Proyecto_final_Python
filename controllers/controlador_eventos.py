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
        indice = self.app.vista_eventos.obtener_evento_seleccionado()
        if indice is not None:
            evento = self.modelo_evento[indice]
            self.app.vista_info.mostrar_info_evento(evento)
            self.app.cambiar_frame(self.app.vista_info)
            
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
        