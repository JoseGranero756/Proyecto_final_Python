import tkinter as tk
from controllers.controlador_mapa import MapViewer

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tour Musical")
        self.geometry("800x600")

        # Crear el botón para mostrar el mapa
        self.btn_show_map = tk.Button(self, text="Ver en Mapa", command=self.show_map)
        self.btn_show_map.pack()

    def show_map(self):
        # Crear una instancia de la clase MapViewer al hacer clic en el botón
        map_window = MapViewer(self, "data/ubicacion.json")
        map_window.show()

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()