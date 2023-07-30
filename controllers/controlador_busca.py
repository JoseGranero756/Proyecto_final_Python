class ControladorBusca:
    def __init__(self,app,modelo_evento):
        self.app = app
        self.modelo_evento = modelo_evento
    
    def obtener_eventos_nombre(self,nombre):
        lista = []
        for evento in self.modelo_evento:
                if nombre.upper() in evento.nombre.upper() :
                    lista.append(evento)
        if  len(lista) > 0:
            return lista
        else:
            text = f"el nombre de evento {nombre} no existe en la base de datos"
            return text
    def obtener_eventos_artista(self,artista):
        lista = []
        for evento in self.modelo_evento:
                if artista.upper() in evento.artista.upper() :
                    lista.append(evento)
        if  len(lista) > 0:
            return lista
        else:
            return f"el artista {artista} no existe en la base de datos"
    def obtener_eventos_genero(self,genero):
        lista = []
        for evento in self.modelo_evento:
                if genero.upper() in evento.genero.upper() :
                    lista.append(evento)
        if  len(lista) > 0:
            return lista
        else:
            return f"el genero {genero} no existe en la base de datos"
    
    def volver_atras(self):
        self.app.cambiar_frame(self.app.vista_busca_filtra)
    
    def seleccionar_evento(self):
        
        indice = self.app.vista_busca.obtener_evento_seleccionado()
        if indice is not None:
            evento = self.modelo_evento[indice]
            self.app.vista_info.mostrar_info_evento(evento)
            self.app.cambiar_frame(self.app.vista_info)
   
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
    
    