import json
import datetime
import tkinter as tk
from tkinter import ttk

class Evento:
    """
    Objeto para guardar los eventos musicales
    """
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
        """
        Convierte a un formato reconocible por json el objeto evento
        """
        return { "tipo" : "evento", "id" : self.id, "nombre" : self.nombre, "artista" : self.artista, "genero" : self.genero, "id ubicacion" : self.id_ubicacion, "hora inicio" : self.hora_inicio, "hora fin" : self.hora_fin, "descripción" : self.descripcion, "imagen" : self.imagen }

class ListaEventos:
    """
    lista de objetos del tipo evento
    """
    def __init__(self,eventos = None):
        if eventos == None:
            self.eventos = []
        else:
            self.eventos = eventos
            
    def agrega_evento(self,evento):
        """
        Agrega un evento a la lista
        """
        self.eventos.append(evento)
    
    def a_json(self):
        """
        Crea una lista de eventos convertidos a un formato admisible para json
        """
        lista = []
        for evento in self.eventos:
            lista.append(evento.a_json)
        return {"Tipo" : "ListaEventos", "Eventos" : lista}
        
class Usuario:
    """
    objeto Usuario para guardar usuarios que asisten a los eventos musicales
    """
    def __init__(self,id,nombre,apellido, usuario, contraseña, historial_eventos = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if historial_eventos == None:
            self.historial_eventos = []
        else:
            self.historial_eventos = historial_eventos    
        self.historial_eventos = historial_eventos
        self.usuario = usuario
        self.contraseña = contraseña
        
    def agregar_evento(self, id_evento):
        """
        Agrega la id de un evento a la lista de eventos a los que asistió el usuario
        """
        self.historial_eventos.append(id_evento)
    
    def a_json(self):
        """
        convierte a Json los datos del usuario
        """
        return {"Tipo" : "Usuario" , "id" : self.id, "Nombre" : self.nombre, "Apellido" : self.apellido, "Historial de eventos" : self.historial_eventos, "Usuario" : self.usuario, "Contraseña" : self.contraseña}

class Lista_Usuarios:
    """
    lista de objetos tipo usuario    
    """
    def __init__(self,usuarios = None):
        if usuarios == None:
            self.usuarios = []
        else:
    
            self.usuarios = usuarios
            
    def agrega_usuario(self,usuario):
        """
        agrega un nuevo usuario a la lista
        """
        self.usuarios.append(usuario)
    
    def a_json(self):
        """
        convierte la lista de objetos tipo usuario a un formato compatiblo con json
        """
        lista = []
        for usuario in self.usuarios:
            lista.append(usuario.a_json)
        return {"Tipo" : "ListaUsuarios" , "Usuarios" : lista}
        
    

class Ubicacion:
    """
    Objeto para la ubicación geografica de los eventos musicales    
    """
    def __init__(self,id,nombre,direccion,coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
    
    def a_json(self):
        """
        convierte el objeto a un formato compatible con json
        """
        return {"Tipo" : "Ubicación" , "id" : self.id, "Nombre" : self.nombre, "Dirección" : self.direccion , "Coordenadas" : self.coordenadas}
        
class Review:
    """
    Objeto con reviews de usuarios sobre cada Evento
    """
    def __init__(self,id,id_evento,id_usuario,calificacion,comentario,animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
        
    def a_json(self):
        """
        conversion a formato legible por json del objeto Review
        """
        return {"Tipo" : "Review", "id" : self.id, "id evento" : self.id_evento, "id usuario": self.id_usuario, "Calificación" : self.calificacion, "Comentario" : self.comentario, "Animo" : self.animo}

class RutaVisita:
    """
    Objeto con rutas para recorrer las ubicaciones de los eventos
    """
    def __init__(self,id,nombre,destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def agregar_destino(self,destino):
        """
        A agrega un destino a la lista de destinos
        """
        self.destinos.append(destino)
        
    def a_json(self):
        """
        convierte el objeto RutaVisita a un formato compatible con Json
        """
        return {"Tipo" : "RutaVisita", "id" : self.id, "Nombre" : self.nombre , "Destinos" : self.destinos}

class ListaJson:
    """
    crea un objeto que va recibir una lista de datos compatibles con JSON
    """
    def __init__(self, lista = None):
        if lista == None:
            self.lista = []
        else:
            self.lista = lista
            
    def agrega_json(self,json):
        """
        agrega un dato a la lista
        """
        self.lista.append(json)
    
        
    
def busca_nombre(eventos,nombre):
    """
    Controla que un nombre exista en la lista de eventos
    """
    i = 0
    b = False
    while i < len(eventos) and b == False:
        if eventos[i].nombre == nombre:
            b =True
    return b

def busca_artista(eventos,artista):
    """
    Controla que un artista exista en la lista de eventos
    """
    i = 0
    b = False
    while i < len(eventos) and b == False:
        if eventos[i].artista == artista:
            b =True
    return b

def busca_genero(eventos,genero):
    """
    Controla que un genero exista en la lista de eventos
    """
    i = 0
    b = False
    while i < len(eventos) and b == False:
        if eventos[i].genero == genero:
            b =True
    return b

def busca_ubicacion(eventos,ubicacion):
    """
    Controla que una ubicación ingresada por el usuario exista
    """
    i = 0
    b = False
    while i < len(eventos) and b == False:
        if eventos[i].ubicacion == ubicacion:
            b =True
    return b


def filtra_por_nombre(eventos):
    """
    filtra los resultados de la lista por nombre, artista o genero
    """
    lista = []
    cursor = "Z"
    while cursor != "S" and len(lista) < 0:
        cursor = input("para buscar por nombre presiona N, para buscar por artista presiona A, para buscar por genero presiona G para salir presiona S") #debería ser reemplazado a la hora de usar tkinter
        while cursor.upper() not in "NAGS":
            print("Ingreso incorrecto")
            cursor = input("para buscar por nombre presiona N, para buscar por artista presiona A, para buscar por genero presiona G para salir presiona S") #debería ser reemplazado a la hora de usar tkinter
        cursor = cursor.upper()
        if cursor == "N":
            nombre = input("Ingrese el nómbre del evento a buscar: ")
            if busca_nombre(eventos,nombre):
                for evento in eventos:
                    if evento.nombre == nombre:
                        lista.append(evento)
                return lista
            else:
                print("Nombre de evento inexistente")
        elif cursor == "A":
            artista = input("Ingrese el Artista del evento a buscar: ")
            if busca_artista(eventos,artista):
                for evento in eventos:
                    if evento.artista == artista:
                        lista.append(evento)
                return lista
            else: 
                print("Nombre de Artista inexistente")
        elif cursor == "G":
            genero = input("Ingrese el genero del evento a buscar: ")
            if busca_genero(eventos,genero):  
                for evento in eventos:
                    if evento.genero == genero:
                        lista.append(evento)
                return lista
            else:
                print("Nombre de genero inexitente")
def filtra_por_ubicacion(eventos):
    lista = []
    cursor = "Z"
    while cursor != "S" and len(lista) < 0:
        cursor = input("para buscar por ubicación presiona U, para buscar por horario presiona H para salir presiona S")
        while cursor.upper() not in "UHS":
            print("ingreso incorrecto, vuelva a ingresar")
            cursor = input("para buscar por ubicación presiona U, para buscar por horario presiona H para salir presiona S")
    if cursor == "U":
        ubicacion = input("escriba la ubicación a filtrar")
        