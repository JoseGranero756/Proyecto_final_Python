import tkinter as tk

class VistaEventosAsistidos(tk.Frame):
    def __init__(self,master = None, controlador = None):
        """
        Crea vista de lista de eventos asistidos.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "Eventos Asistidos")
        self.titulo.pack(pady=10)
        
        # Crea la listbox donde se van a ver los evnetnos asistidos
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        
        # Asocia el evento de doble click a la función seleccionar_evento_asistido.
        self.listbox.bind("<Double-Button-1>",self.seleccionar_evento_asistido)
        
        self.listbox.pack(pady=10)
        self.actualizar_eventos_asistidos()
        
        # Crea el botón para ir a inicio y lo agrega a la vista.
        self.boton_inicio = tk.Button(
            self,text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.pack(pady=10)
        
    def actualizar_eventos_asistidos(self):
        """
        Actualiza la lista de eventos asistidos con los eventos obtenidos en contolador.
        
        """
        eventos = self.controlador.obtener_eventos_asistidos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)
    def obtener_evento_asistido_seleccionado(self):
        """
        Retorna el indice del evento seleccionado en la lista.
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None
    def seleccionar_evento_asistido(self,event):
        """
        Obtiene el índice del evento seleccionado y llama al controlador para
        mostrar la información del evento.
        """
        self.controlador.seleccionar_evento_asistido()