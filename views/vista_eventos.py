import tkinter as tk

class VistaEventos(tk.Frame):
    def __init__(self,master = None, controlador = None):
        """
        Crea la vista de la lista de eventos.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "lista de eventos")
        self.titulo.pack(pady=10)
        
        # Crea la listbox donde se va a ver la lista de eventos.
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        
        # Asocia el evento de doble click a la función seleccionar_evento.
        self.listbox.bind("<Double-Button-1>",self.seleccionar_evento)
        
        self.listbox.pack(pady=10)
        
        # Llama a la función actualizar eventos.
        self.actualizar_eventos() 
        
        # Crea el botón para ir a inicio y lo agrega a la vista.
        self.boton_inicio = tk.Button(
            self,text = "Ir al Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.pack(pady=10)
        
    def actualizar_eventos(self):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador.
        """
        eventos = self.controlador.obtener_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)
    
    def obtener_evento_seleccionado(self):
        """
        Retorna el indice del evento seleccionado en la lista
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None
    
    def seleccionar_evento(self,event):
        """
        Obtiene el índice del evento seleccionado y llama al controlador para
        mostrar la información del evento.
        """
        self.controlador.seleccionar_evento()
            
        
    