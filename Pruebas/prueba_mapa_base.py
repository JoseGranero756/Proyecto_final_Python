import tkinter as tk
import tkintermapview

mapa = tk.Tk()
mapa.geometry("800x600")
mapa.title("Explora los lugares")

# crea widget de mapa
map_widget = tkintermapview.TkinterMapView(mapa, width=800, height=600, corner_radius=0)
map_widget.place(x=0, y=0)

# setea la posición y el zoom del widget
map_widget.set_position(-24.7881269439682, -65.41631940688363)  # posición inicial
map_widget.set_zoom(13)

mapa.mainloop()
