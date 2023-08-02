class ControladorBusca:
    def __init__(self,app,modelo_evento,modelo_ubicacion):
        self.app = app
        # Lista de eventos cargado del json evento
        self.modelo_evento = modelo_evento
        # Lista de ubicaciones cargada del json ubicacion
        self.modelo_ubicacion = modelo_ubicacion
    
    def obtener_eventos_nombre(self,nombre):
        """
        Obtiene una lista de eventos que contengan un nombre determinado en su nombre
        """
        lista = []
        for evento in self.modelo_evento:
                if nombre.upper() in evento.nombre.upper() :
                    lista.append(evento)
        if  len(lista) > 0:
            return lista
        else:
            # Si no hay coincidencias, devuelve un string con el error
            text = f"el nombre de evento {nombre} no existe en la base de datos" 
            return text
   
    def obtener_eventos_artista(self,artista):
        """
        Obtiene una lista de eventos que contengan un nombre artista determinado en su categoría artista
        """
        lista = []
        for evento in self.modelo_evento:
                if artista.upper() in evento.artista.upper() :
                    lista.append(evento)
        if  len(lista) > 0:
            return lista
        else:
            # Si no hay coincidencias, devuelve un string con el error
            return f"el artista {artista} no existe en la base de datos"
    
    def obtener_eventos_genero(self,genero):
        """
        Obtiene una lista de eventos que contengan un nombre de genero determinado en su categoría genero
        """
        lista = []
        for evento in self.modelo_evento:
            if genero.upper() in evento.genero.upper() :
                lista.append(evento)
        if  len(lista) > 0:
            return lista
        else:
            # Si no hay coincidencias, devuelve un string con el error
            return f"el genero {genero} no existe en la base de datos"
    
    def filtrar_eventos_nombre_hora(self,nombre):
        """
        Crea una lista de horas asociadas a un evento filtrado por un nombre dado y quitando repetidas
        """
        lista = self.obtener_eventos_nombre(nombre)
        horas = []
        eventos = []
        if type(lista) == list:
            for evento in lista:
                if evento.hora_inicio not in horas:
                    horas.append(evento.hora_inicio)
                    eventos.append(evento)
            return(eventos)
    
    def filtrar_eventos_artista_hora(self,artista):
        """
        Crea una lista de horas asociadas a un evento filtrado por un artista dado y quitando horas repetidas
        """
        lista = self.obtener_eventos_artista(artista)
        horas = []
        eventos = []
        if type(lista) == list:
            for evento in lista:
                if evento.hora_inicio not in horas:
                    horas.append(evento.hora_inicio)
                    eventos.append(evento)
            return(eventos)
    
    def filtrar_eventos_genero_hora(self,genero):
        """
        Crea una lista de horas asociadas a un evento filtrado por un genero dado y quitando horas repetidas
        """
        lista = self.obtener_eventos_genero(genero)
        horas = []
        eventos = []
        if type(lista) == list:
            for evento in lista:
                if evento.hora_inicio not in horas:
                    horas.append(evento.hora_inicio)
                    eventos.append(evento)
            return(eventos)
        
    def filtrar_eventos_nombre_ubicacion(self,eventos):
        """
        Crea una lista de ubicaciones para mostrar en la listbox filtro_ubicaciones.
        """
        ubicaciones = []
        if type(eventos) == list:
            for evento in eventos:
                if self.modelo_ubicacion[evento.id_ubicacion] not in ubicaciones:
                    ubicaciones.append(self.modelo_ubicacion[evento.id_ubicacion])
            return ubicaciones
        
    
    def filtrar_hora_nombre(self,hora,nombre):
        """
        Obtiene los eventos que coincidan con un nombre y hora especificos
        """
        lista = []
        eventos = self.obtener_eventos_nombre(nombre)
        for evento in eventos:
            if hora == evento.hora_inicio:
                lista.append(evento)
        return lista
    
    def filtrar_hora_artista(self,hora,artista):
        """
        Obtiene los eventos que coincidan con un artista y hora especificos
        """
        lista = []
        eventos = self.obtener_eventos_artista(artista)
        for evento in eventos:
            if hora == evento.hora_inicio:
                lista.append(evento)
        return lista
    
    def filtrar_hora_genero(self,hora,genero):
        """
        Obtiene los eventos que coincidan con un genero y hora especificos
        """
        lista = []
        eventos = self.obtener_eventos_genero(genero)
        for evento in eventos:
            if hora == evento.hora_inicio:
                lista.append(evento)
        return lista
    
    
    def seleccionar_evento(self):
        """
        Selecciona un evento de la listbox principal, lo pasa a vista_info y cambia el frame a esa vista
        """
        indice = self.app.vista_busca.obtener_evento_seleccionado()
        if indice is not None:
            evento = self.modelo_evento[indice]
            self.app.vista_info.mostrar_info_evento(evento)
            self.app.cambiar_frame(self.app.vista_info)
    
    def regresar_inicio(self):
        """
        Regresa al frame vista_inicio
        """
        self.app.cambiar_frame(self.app.vista_inicio)
    
    