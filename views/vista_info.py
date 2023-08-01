import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un evento.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.evento_label = tk.Label(self, text="",font = ("Open Sans", 15),width=50)
        self.evento_label.pack(pady=50)
        self.evento_label.config(justify=tk.LEFT)
        
        self.boton_volver_inicio = tk.Button(
            self,
            text="Ir al inicio",
            command=self.controlador.volver_inicio,
        )
        self.boton_volver_inicio.pack(pady=10)
        
    def mostrar_info_evento(self, evento):
        """
        Muestra la información del evento recibido como parámetro.
        """
        info = f"Nombre: {evento.nombre}\nArtista: {evento.artista}\nGenero: {evento.genero}\nUbicación{evento.id_ubicacion}\nHora de inicio:{evento.hora_inicio}\nHora Fin:{evento.hora_fin}\nDescripción:{evento.descripcion}"
        self.evento_label["text"] = info
        
        
