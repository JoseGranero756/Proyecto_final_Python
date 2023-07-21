import json
import datetime
class Evento:
    def __init__(
            self,
            id_evento, #modifique nombre id para mas claridad.
            nombre,
            artista,
            genero,
            id_ubicacion,
            hora_inicio,
            hora_fin,
            descripcion,
            imagen):
        
        self.id_evento = id_evento
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen
        
    def a_json(self):
        return { 
                "Tipo" : "Evento", 
                "id" : self.id_evento, 
                "Nombre" : self.nombre, 
                "Artista" : self.artista, 
                "Genero" : self.genero, 
                "id ubicación" : self.id_ubiacion, 
                "Hora inicio" : self.hora_inicio, 
                "Hora fin" : self.hora_fin, 
                "Descripción" : self.descripcion, 
                "Imagen" : self.imagen
                }
    
class Usuario:
    
    def __init__(self,id_usuario,nombre,apellido): #suprimi historial evento ya que empieza en []
        self.id_usuario = id_usuario #cambie por id usuario
        self.nombre = nombre
        self.apellido = apellido
        #self.historial_eventos = historial_eventos
        #El historial cuando inicia empieza en vacio siempre. despues se agregan eventos con agregar eventos
        self.historial_evento = []

    def agregar_evento(self, id_evento):
        self.historial_eventos.append(id_evento) #Serecibe un id_evento
    
    def a_json(self):
        return {
                "Tipo" : "Usuario",
                "id" : self.id_usuario, 
                "Nombre" : self.nombre, 
                "Apellido" : self.apellido, 
                "Historial de eventos" : self.historial_evento 
                # ver como pasar el historial de evento a json
                }

class Ubicacion:
    def __init__(self, id_ubicacion, nombre ,direccion , coordenadas):
        self.id_ubicacion = id_ubicacion 
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas #Latitud y longitud
    
    def a_json(self):
        return {
                "Tipo" : "Ubicación" , 
                "id" : self.id_ubicacion, 
                "Nombre" : self.nombre, 
                "Dirección" : self.direccion, 
                "Coordenadas" : self.coordenadas
                #Si queremos que esto vaya a json calculo que queremos que esto sea ya convertido a texto 
                }
        
class Review:
    def __init__(self, id_review, id_evento, id_usuario, calificacion , comentario, animo):
        self.id = id_review
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
        
    def a_json(self):
        return {"Tipo" : "Review", 
                "id" : self.id, 
                "id evento" : self.id_evento, 
                "id usuario": self.id_usuario, 
                "Calificación" : self.calificacion, 
                "Comentario" : self.comentario, 
                "Animo" : self.animo}

class RutaVisita:
    def __init__(self,id,nombre,destinos): #No entiendo que hace destino pero creo que deberia empezar en [] si lo vamos a ir agregando.
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def agregar_destino(self,destino):
        self.destinos.append(destino)
        
    def a_json(self):
        return {"Tipo" : "RutaVisita", 
                "id" : self.id, 
                "Nombre" : self.nombre, 
                "Destinos" : self.destinos}
    