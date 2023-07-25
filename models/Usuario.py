import json

class Usuario:
    
    def __init__(self,id_usuario,nombre,apellido,historial_eventos=[]): #suprimi historial evento ya que empieza en []
        self.id_usuario = id_usuario #cambie por id usuario
        self.nombre = nombre
        self.apellido = apellido
        #self.historial_eventos = historial_eventos
        #El historial cuando inicia empieza en vacio siempre. despues se agregan eventos con agregar eventos
        self.historial_eventos = historial_eventos

    def agregar_evento(self, id_evento):
        self.historial_eventos.append(id_evento) #Serecibe un id_evento

    @classmethod
    def de_json(cls, json_dato):
        """Devuelve un ojeto de tipo de esta clase."""
        id_usuario = json_dato["id_usuario"]
        nombre = json_dato["nombre"]
        apellido = json_dato["apellido"]
        historial_evento = json_dato["historial_evento"]
        return cls(id_usuario, nombre, apellido, historial_evento)        

    def a_json(self):
        """Devuelve un diccionario con la informacion del objeto."""
        return {
                "Tipo" : "Usuario",
                "id" : self.id_usuario, 
                "Nombre" : self.nombre, 
                "Apellido" : self.apellido, 
                "Historial de eventos" : self.historial_eventos 
                # ver como pasar el historial de evento a json
                }