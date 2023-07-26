import tkinter as tk
import customtkinter as ctk
import json
import datetime
import tkinter as tk
from models.Evento import Evento
from models.Usuario import Usuario
from models.Review import Review
from models.RutaVisita import RutaVisita
from models.Ubicación import Ubicacion
from views.vista_eventos import VistaEventos
from views.vista_inicio import VistaInicio
from views.vista_info import VistaInfo
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_eventos import ControladorEventos
from controllers.controlador_info import ControladorInfo


class aplicacion(tk.Tk):
    def __init__(self):
        tk.TK.__init__(self)
        self.title("Tour de musica")
        self.geometry("330x300")
        self.resizable(False,False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)
    
    def inicializar(self):
        eventos = Evento.de_json(data/evento.json)
        
        controlador_inicio = ControladorInicio(self)
        controlador_eventos = ControladorEventos(self,eventos)
        controlador_info = ControladorInfo(self)
        
        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_eventos = VistaEventos(self, controlador_eventos)
        self.vista_info = VistaInfo(self, controlador_info)
        


        
        
        