class ControladorBusca:
    def __init__(self,app,modelo_evento):
        self.app = app
        self.modelo_evento = modelo_evento
    
    def obtener_eventos_nombre(self,nombre):
        lista = []
        for evento in self.modelo_evento:
            if evento.nombre.upper() == nombre.upper():
                lista.append(evento)
        if len(lista) > 0:
            return lista
        else:
            return False
        
    def obtener_eventos_artista(self,artista):
        lista = []
        for evento in self.modelo_evento:
            if evento.nombre.upper() == artista.upper():
                lista.append(evento)
        if len(lista) > 0:
            return lista
        else:
            return False
        
    def obtener_eventos_genero(self,genero):
        lista = []
        for evento in self.modelo_evento:
            if evento.nombre.upper() == genero.upper():
                lista.append(evento)
        if len(lista) > 0:
            return lista
        else:
            return False
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