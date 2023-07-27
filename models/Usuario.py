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
        historial_eventos = json_dato["historial_eventos"]
        return cls(id_usuario, nombre, apellido, historial_eventos)        

    def a_json(self):
        """Devuelve un diccionario con la informacion del objeto."""
        return {
                "Tipo" : "Usuario",
                "id_usuario" : self.id_usuario, 
                "nombre" : self.nombre, 
                "apellido" : self.apellido, 
                "historial_eventos" : self.historial_eventos 
                # ver como pasar el historial de evento a json
                }
    
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            json_usuarios = json.load(f)
        lista_objeto_usuario = []
        for json_usuario in json_usuarios:
            del json_usuario["Tipo"]
            usuario_objeto = cls.de_json(json_usuario)
            lista_objeto_usuario.append(usuario_objeto)    
        return lista_objeto_usuario     