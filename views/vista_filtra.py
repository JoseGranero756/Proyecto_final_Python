import tkinter as tk

class VistaFiltra(tk.Frame):
    def __init__(self,master = None, controlador = None):
        
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "Filtrado")
        self.titulo.grid(row=0,columnspan=3)
        
        