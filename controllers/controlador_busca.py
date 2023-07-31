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
    
    def filtrar_eventos_nombre_hora(self,nombre):
        lista = self.obtener_eventos_nombre(nombre)
        horas = []
        eventos = []
        if type(lista) == list:
            for evento in lista:
                if evento.hora_inicio not in horas:
                    horas.append(evento.hora_inicio)
                    eventos.append(evento)
            return(eventos)
    
    def filtrar_eventos_nombre_artista(self,nombre):
        lista = self.obtener_eventos_artista(nombre)
        horas = []
        eventos = []
        if type(lista) == list:
            for evento in lista:
                if evento.hora_inicio not in horas:
                    horas.append(evento.hora_inicio)
                    eventos.append(evento)
            return(eventos)
    
    def filtrar_eventos_nombre_genero(self,genero):
        lista = self.obtener_eventos_genero(genero)
        horas = []
        eventos = []
        if type(lista) == list:
            for evento in lista:
                if evento.hora_inicio not in horas:
                    horas.append(evento.hora_inicio)
                    eventos.append(evento)
            return(eventos)
    
    def filtrar_hora_nombre(self,hora,nombre):
        lista = []
        eventos = self.obtener_eventos_nombre(nombre)
        for evento in eventos:
            if hora == evento.hora_inicio:
                lista.append(evento)
        return lista
    
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
    
    