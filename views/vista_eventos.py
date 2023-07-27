import tkinter as tk

class VistaEventos(tk.Frame):
    def __init__(self,master = None, controlador = None):
        """
        Crea la vista de la lista de eventos.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "lista de eventos")
        self.titulo.pack(pady=10)
        
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        
        # Asocia el evento de doble click a la función seleccionar_evento
    