import tkinter as tk

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
        info = f"id: {evento.id_evento}\nNombre: {evento.nombre}\nArtista: {evento.artista}\ngenero: {evento.genero}\nid_ubicación{evento.id_ubicacion}\nHora de inicio:{evento.hora_inicio}\nHora Fin:{evento.hora_fin}\nDescripción:{evento.descripcion}\nImagen{evento.imagen}"
        self.evento_label["text"] = info