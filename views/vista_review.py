import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import json
import sys
sys.path.append(r'.\models')
from Review import Review
sys.path.append(r'.\controllers')
from controlador_review import ControladorReview 
class VistaReview(tk.Frame):
    def __init__(self,master = None, controlador = None):
        """
        Crea la vista de reviews
        """
        
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.evento = None
        self.id_review = None

        label_titulo = tk.Label(self, text="Review", font=("Helvetica", 20))
        label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="we")
        
        self.calificacion_label = tk.Label(self, text="Calificación:",font = ("Open Sans", 15),width=50)
        self.calificacion_label.grid(row=1, column=0, padx=5, pady=5)
        self.calificacion_label.config(justify=tk.LEFT)

        opciones = [1,2, 3, 4, 5]
        self.calificacion_combo_box = ttk.Combobox(self, values=opciones)
        self.calificacion_combo_box.grid(row=1, column=1, padx=5, pady=5)

        # self.calificacion_entry = tk.Entry(self)
        # self.calificacion_entry.grid(row=1, column=1, padx=5, pady=5)

        self.comentario_label = tk.Label(self, text="Comentario:",font = ("Open Sans", 15),width=50)
        self.comentario_label.grid(row=2, column=0, padx=5, pady=5)
        self.comentario_label.config(justify=tk.LEFT)

        self.comentario_entry = tk.Entry(self,width=50)
        self.comentario_entry.grid(row=2, column=1, padx=5, pady=5)
  

        self.animo_label = tk.Label(self, text="Animo:",font = ("Open Sans", 15),width=50)
        self.animo_label.grid(row=3, column=0, padx=5, pady=5)
        self.animo_label.config(justify=tk.LEFT)

        # self.animo_entry = tk.Entry(self)
        # self.animo_entry.grid(row=2, column=1, padx=5, pady=5) 
        self.animo = tk.IntVar()
        self.radio1_animo = tk.Radiobutton(self, text="Positivo", variable=self.animo, value=0,command= lambda: print("Buena"))
        self.radio1_animo.grid(row=3, column=1, padx=5, pady=5)

        self.radio1_animo = tk.Radiobutton(self, text="Negativo", variable=self.animo, value=1, command= lambda: print("Mala") )
        self.radio1_animo.grid(row=4, column=1, padx=5, pady=5)

        self.boton_guardar = tk.Button(
            self,
            text="Guardar",
            command = lambda: self.controlador.guardar(self.controlador.conseguir_id_review(),self.evento.id_evento, 2, int(self.calificacion_combo_box.get()), self.comentario_entry.get(), self.animo.get())
        )
        self.boton_guardar.grid(row=5, column=1, padx=5, pady=5)

        self.boton_volver_inicio = tk.Button(
        self,
        text="Ir al inicio",
        command=self.controlador.volver_inicio,
        )
        self.boton_volver_inicio.grid(row=6, column=1, padx=5, pady=5)



    def hacer_review(self,evento):
        self.evento = evento
        print(type(evento))
        print(type(evento))
    
    # def conseguir_id_review(self):
    #     self.id_review = self.controlador.conseguir_id_review()