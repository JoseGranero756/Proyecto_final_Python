import tkinter as tk

class VistaBusca(tk.Frame):
    def __init__(self,master = None, controlador = None):
        
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "Busqueda de eventos")
        self.descripcion_nombre = tk.Label(self,text = "Busca eventos con el mismo nombre")
        self.descripcion_artista = tk.Label(self,text = "Busca eventos con el mismo artista")
        self.descripcion_genero = tk.Label(self,text = "Busca eventos con el mismo genero musical")
        
        self.titulo.grid(row=0,columnspan=3)
        self.descripcion_nombre.grid(row=1,column=0)
        self.descripcion_artista.grid(row=1,column=1)
        self.descripcion_genero.grid(row=1,column=2)
        
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=80)
        
        self.listbox.bind("<Double-Button-1>",self.seleccionar_evento)
        
        self.listbox.grid(pady=10,row=5,column=1)
        
        texto = tk.Entry(self)
        texto.grid(pady = 5, row = 2,columnspan=3,)
        texto.delete(0,tk.END)
        
        self.boton_nombre = tk.Button(
            self,
            text="Busca por nombre",
            command = lambda : self.actualizar_eventos_nombre(texto.get()),
        )
        self.boton_artista = tk.Button(
            self,
            text="Busca por artista",
            command = lambda : self.actualizar_eventos_artista(texto.get()),
        )
        self.boton_genero = tk.Button(
            self,
            text="busca por genero",
            command = lambda : self.actualizar_eventos_genero(texto.get()),
        )
        self.boton_volver = tk.Button(
            self,
            text = "Volver Atras",
            command=controlador.volver_atras,
        )
        self.boton_inicio = tk.Button(
            self,
            text = "Ir al inicio",
            command=self.controlador.regresar_inicio,
        )
        
        self.boton_nombre.grid(pady = 5,row=3,column=0)
        self.boton_artista.grid(pady = 5,row=3,column=1)
        self.boton_genero.grid(pady = 5,row=3,column=2)
        self.boton_volver.grid(pady = 5,row=4,column=1)
        self.boton_inicio.grid(pady = 5,row=4,column=2)
        
    def actualizar_eventos_nombre(self,nombre):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador.
        """
        eventos = self.controlador.obtener_eventos_nombre(nombre)
        if type(eventos) == list:
            self.listbox.delete(0, tk.END)
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        else:
            self.listbox.delete(0,tk.END)
            self.listbox.insert(tk.END,f"{eventos}")
    
    def actualizar_eventos_artista(self,artista):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador.
        """
        eventos = self.controlador.obtener_eventos_artista(artista)
        if type(eventos) == list:
            self.listbox.delete(0, tk.END)
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        else:
            self.listbox.delete(0,tk.END)
            self.listbox.insert(tk.END,f"{eventos}")
    
    def actualizar_eventos_genero(self,genero):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador.
        """
        eventos = self.controlador.obtener_eventos_genero(genero)
        if type(eventos) == list:
            self.listbox.delete(0, tk.END)
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        else:
            self.listbox.delete(0,tk.END)
            self.listbox.insert(tk.END,f"{eventos}")
    
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