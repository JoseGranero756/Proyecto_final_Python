import tkinter as tk

class VistaBuscaFiltra(tk.Frame):
    def __init__(self, master = None, controlador = None):
        
        
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "Busqueda/Filtrado")
        self.titulo.grid(row=0,columnspan=3)
        
        self.descripcion_busca = tk.Label(self,text="busca un evento por nombre de evento, artista, genero")
        self.descripcion_filtra = tk.Label(self,text="filtra eventos por hora de inicio y ubicación")
        self.boton_busca = tk.Button(
            self,
            text = "buscar",
            command=self.controlador.busca,
        )
        self.boton_filtra = tk.Button(
            self,
            text = "Filtra",
            command=self.controlador.filtra,
        )
        self.boton_inicio = tk.Button(
            self,
            text = "ir a inicio",
            command=self.controlador.regresar_inicio,
        )
        
        self.descripcion_busca.grid(row=1, column=0)
        self.descripcion_filtra.grid(row=1,column=1)
        self.boton_busca.grid(row=2,column=0)
        self.boton_filtra.grid(row=2,column=1)
        self.boton_inicio.grid(row=4,columnspan=3)
        