import tkinter as tk
from tkinter.font import Font

class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="Tour musical", font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=5)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(size=12)

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion_lista = tk.Label(
            self,
            text="Aquí puedes revisar los eventos con información detallada.",
            font=descripcion_font,
            wraplength=200,
        )
        self.descripcion_asistidos = tk.Label(
            self,
            text="aquí puedes revisar los eventos a los que asististe",
            font=descripcion_font,
            wraplength=200,
        )
        self.descripcion_busqueda = tk.Label(
            self,
            text="aquí puedes buscar y filtrar eventos",
            font=descripcion_font,
            wraplength=200,
        )
        self.descripcion_lista.grid(row=1, column=0)
        self.descripcion_asistidos.grid(row=1, column=1)
        self.descripcion_busqueda.grid(row=1,column=2)
        

        # Crea el botón para ir a los eventos asistidos y lo agrega a la vista
        self.boton_eventos = tk.Button(
            self, text="Ver eventos", command=self.controlador.mostrar_eventos
        )
        self.boton_asistidos = tk.Button(
              self, text="Ver asistidos", command=self.controlador.mostrar_asistidos
        )
        self.boton_busqueda = tk.Button(
            self, text="buscar/filtrar", #command=self.controlador.mostrar_busqueda
        )
        self.boton_eventos.grid(row=2, column=0)
        self.boton_asistidos.grid(row=2, column=1)
        self.boton_busqueda.grid(row=2, column=2)