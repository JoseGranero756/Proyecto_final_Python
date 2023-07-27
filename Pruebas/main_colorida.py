import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TourMusicalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tour Musical")
        self.geometry("700x600")  # Ajusta la geometría según tus necesidades
        self.configure(bg="green", )  # Establecer el color de fondo verde de la aplicación

        self.create_widgets()

    def create_widgets(self):
        # Agregar el título con una tipografía moderna y llamativa
        title_label = tk.Label(self, text="Tour Musical", font=("Helvetica", 40, "bold"), fg="white", bg="green")
        title_label.pack(pady=50)

        # Crear un frame para el cuerpo de la pantalla principal
        body_frame = tk.Frame(self, bg="#E5E5E5", bd=3, relief="solid", borderwidth=4)
        body_frame.pack(fill=tk.BOTH, expand=True)

        # Agregar los botones interactivos de color amarillo usando tk.Button
        index_button = tk.Button(body_frame, bg="yellow", text="Índice de eventos", command=self.mostrar_indice_eventos,
                                 font=("Helvetica", 16, "bold"))
        index_button.pack(pady=20)

        search_button = tk.Button(body_frame, bg="yellow", text="Búsqueda y filtrado de eventos", command=self.mostrar_herramienta_busqueda,
                                  font=("Helvetica", 16, "bold"))
        search_button.pack(pady=20)

        history_button = tk.Button(body_frame, bg="yellow", text="Historial de eventos", command=self.mostrar_historial_eventos,
                                   font=("Helvetica", 16, "bold"))
        history_button.pack(pady=20)

        # Configurar los bordes verdes en el widget principal
        self.configure(borderwidth=4, relief="solid")

    def mostrar_indice_eventos(self):
        print("Mostrando índice de eventos")

    def mostrar_herramienta_busqueda(self):
        print("Mostrando herramienta de búsqueda y filtrado de eventos")

    def mostrar_historial_eventos(self):
        print("Mostrando historial de eventos")

if __name__ == "__main__":
     app = TourMusicalApp()
     app.mainloop()
    
    









