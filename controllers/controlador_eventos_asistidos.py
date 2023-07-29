class ControladorEventosAsistidos:
    def __init__(self,app,modelo_usuario,modelo_evento):
        self.app = app
        self.modelo_usuario = modelo_usuario
        self.modelo_evento = modelo_evento
        self.lista_asistidos = []
    def obtener_eventos_asistidos(self):
        """
        obtiene una lista de los eventos que coinciden en id con los asistidos por el usuario
        """
        if len(self.modelo_usuario.historial_eventos) > 0:
            for evento in self.modelo_evento:
                if evento.id_evento in self.modelo_usuario.historial_eventos:
                    self.lista_asistidos.append(evento)
        return self.lista_asistidos
    def seleccionar_evento_asistido(self):
        """
        obtiene el indice del evento seleccionado y llama a la vista de
        información para mostrar la informacion del evento
        """
        indice = self.app.vista_eventos_asistidos.obtener_evento_asistido_seleccionado()
        if indice is not None:
            evento = self.modelo_evento[indice]
            self.app.vista_info.mostrar_info_evento(evento)
            self.app.cambiar_frame(self.app.vista_info)
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)