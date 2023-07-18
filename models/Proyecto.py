import json
import datetime
class Evento:
    def __init__(self,id,nombre,artista,genero,id_ubicacion,hora_inicio,hora_fin,descripcion,imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen
        
    def a_json(self):
        return { "Tipo" : "Evento", "id" : self.id, "Nombre" : self.nombre, "Artista" : self.artista, "Genero" : self.genero, "id ubicación" : self.id_ubiacion, "Hora inicio" : self.hora_inicio, "Hora fin" : self.hora_fin, "Descripción" : self.descripcion, "Imagen" : self.imagen }
    
class Usuario:
    def __init__(self,id,nombre,apellido,historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos
        
    def agregar_evento(self, evento):
        self.historial_eventos.append(evento)
    
    def a_json(self):
        return {"Tipo" : "Usuario" , "id" : self.id, "Nombre" : self.nombre, "Apellido" : self.apellido, "Historial de eventos" : self.historial_eventos}

class Ubicacion:
    def __init__(self,id,nombre,direccion,coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
    
    def a_json(self):
        return {"Tipo" : "Ubicación" , "id" : self.id, "Nombre" : self.nombre, "Dirección" : self.direccion , "Coordenadas" : self.coordenadas}
        
class Review:
    def __init__(self,id,id_evento,id_usuario,calificacion,comentario,animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
        
    def a_json(self):
        return {"Tipo" : "Review", "id" : self.id, "id evento" : self.id_evento, "id usuario": self.id_usuario, "Calificación" : self.calificacion, "Comentario" : self.comentario, "Animo" : self.animo}

class RutaVisita:
    def __init__(self,id,nombre,destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def agregar_destino(self,destino):
        self.destinos.append(destino)
        
    def a_json(self):
        return {"Tipo" : "RutaVisita", "id" : self.id, "Nombre" : self.nombre , "Destinos" : self.destinos}