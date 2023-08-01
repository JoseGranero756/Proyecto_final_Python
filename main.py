import tkinter as tk
from tkinter import *
from models.Evento import Evento
from models.Usuario import Usuario
from models.Review import Review
from models.RutaVisita import RutaVisita
from models.Ubicación import Ubicacion

from views.vista_eventos import VistaEventos
from views.vista_inicio import VistaInicio
from views.vista_info import VistaInfo
from views.vista_eventos_asistidos import VistaEventosAsistidos
from views.vista_busca import VistaBusca

from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_eventos import ControladorEventos
from controllers.controlador_info import ControladorInfo
from controllers.controlador_eventos_asistidos import ControladorEventosAsistidos
from controllers.controlador_busca import ControladorBusca

class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tour de musica")
        self.geometry("850x350")
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)
        self.configure(bg="#E5E5E5")
    
    def inicializar(self):
        """
        Inicializa los objetos del programa
        """
        eventos = Evento.cargar_de_json("data/evento.json") 
        reviews = Review.cargar_de_json("data/review.json")
        usuarios = Usuario.cargar_de_json("data/usuario.json")
        ubicacion = Ubicacion.cargar_de_json("data/ubicacion.json")
        
        usuario_activo = usuarios[2] # Carga el usuario en el indice 2 de la lista de usuarios
         
        controlador_inicio = ControladorInicio(self) 
        controlador_eventos = ControladorEventos(self,eventos)
        controlador_eventos_asistidos = ControladorEventosAsistidos(self,usuario_activo,eventos)
        controlador_info = ControladorInfo(self)
        controlador_busca = ControladorBusca(self,eventos,ubicacion)
        
        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_eventos = VistaEventos(self, controlador_eventos)
        self.vista_info = VistaInfo(self, controlador_info)
        self.vista_eventos_asistidos = VistaEventosAsistidos(self,controlador_eventos_asistidos)
        self.vista_busca = VistaBusca(self,controlador_busca)
        self.vista_busca.place(width=850,height=350)
        
        
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_info)
        self.ajustar_frame(self.vista_eventos_asistidos)
        self.ajustar_frame(self.vista_busca)
        
    def ajustar_frame(self, frame):
        """
        Ajusta el frame del programa
        """
        frame.grid(row=0, column=0, sticky = N+S+E+W)
        
    def cambiar_frame(self, frame_destino):
        """
        Cambia la vista de frame del programa por un frame dado
        """
        frame_destino.tkraise()
    
    def destruir_frame(self, frame):
        """
        Destruye un frame dado
        """
        frame.destroy()
        
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
        
        


        
        
        