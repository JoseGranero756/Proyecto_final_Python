import tkinter as tk
import tkintermapview
import json

class MapViewer:
    def __init__(self, parent, json_file):
        self.parent = parent
        self.map_window = tk.Toplevel(self.parent)
        self.map_window.title("Mapa de Eventos")
        self.map_window.geometry("800x600")

        self.map_widget = tkintermapview.TkinterMapView(self.map_window, width=800, height=600, corner_radius=0)
        self.map_widget.place(x=0, y=0)

        self.map_widget.set_position(-24.782867187531163, -65.41728426257843)  # posición inicial
        self.map_widget.set_zoom(15)

        self.points = []  # Lista para almacenar los puntos de los eventos

        # Leer los datos de los puntos de eventos desde el archivo .json
        self.load_points_from_json(json_file)

    def load_points_from_json(self, json_file):
        with open(json_file, "r") as file:
            data = json.load(file)

        for event in data:
            lat, lon = event["coordenadas"]
            self.add_event_marker(lat, lon)

    def add_event_marker(self, lat, lon):
        # Agregamos el punto como marcador al mapa
        self.map_widget.set_marker(lat, lon)

    # No incluimos la funcionalidad de mostrar imágenes emergentes

if __name__ == "__main__":
    app = MapViewer(None, "data/ubicacion.json")
    app.mainloop()
