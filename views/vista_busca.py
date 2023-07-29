import tkinter as tk

class VistaBusca(tk.Frame):
    def __init__(self,master = None, controlador = None):
        
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.label(self,text = "busqueda de eventos")
        self.titulo.pack(pady=10)
        
        self.boton_nombre = tk.Button(
            self,
            text="Busca por nombre",
        
        )