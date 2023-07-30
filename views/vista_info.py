import tkinter as tk
from PIL import Image, ImageTk

class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un evento.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.evento_label = tk.Label(self, text="")
        self.evento_label.pack(pady=50)
        self.evento_label.config(justify=tk.LEFT)
        self.boton_ir_lista_eventos = tk.Button(
            self,
            text="ir a la lista de completa de eventos",
            command=self.controlador.regresar_eventos,
        )
        self.boton_ir_lista_asistidos = tk.Button(
            self,
            text="ir a la lista de eventos asistidos",
            command=self.controlador.regresar_eventos_asistidos,
        )
        self.boton_ir_lista_eventos.pack(pady=10)
        self.boton_ir_lista_asistidos.pack(pady=30)

    def mostrar_info_evento(self, evento):
        """
        Muestra la información del evento recibido como parámetro.
        """
        info = f"Nombre: {evento.nombre}\nArtista: {evento.artista}\nGenero: {evento.genero}\nid_ubicación{evento.id_ubicacion}\nHora de inicio:{evento.hora_inicio}\nHora Fin:{evento.hora_fin}\nDescripción:{evento.descripcion}"
        self.evento_label["text"] = info
        # mostrar imagen
        if hasattr(self, "image_label"):
            self.image_label.pack_forget()
        path_imagen = f"{evento.imagen}"
        try:
            image = Image.open(path_imagen)
            image = image.resize((200, 200))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Crear un widget Label para mostrar la imagen
            image_label = tk.Label(self, image=photo)
            image_label.image = photo  # Conserva una referencia para evitar que la imagen sea eliminada por el recolector de basura
            image_label.pack(pady=10)  # Agrega un espaciado entre la información del evento y la imagen

        except FileNotFoundError:
            # En caso de que no se encuentre la imagen, muestra un mensaje de error o simplemente ignora esta parte
            print("Imágen no disponible.")
