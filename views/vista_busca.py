import tkinter as tk
from tkinter.font import Font 

class VistaBusca(tk.Frame):
    def __init__(self,master = None, controlador = None):
        
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "Busqueda de eventos", font = ("Roboto",20))
        
        self.bandera = None # Bandera para controlar por que categoría se buscó al ultimo
        
        self.descripcion_nombre = tk.Label(self,text = "Buscar eventos por nombre",font = ("Open Sans",15))
        self.descripcion_artista = tk.Label(self,text = "Buscar eventos por artista",font = ("Open Sans",15))
        self.descripcion_genero = tk.Label(self,text = "Buscar eventos por genero",font = ("Open Sans",15))
        self.descripcion_entry = tk.Label(self,text = "Buscar escribiendo aquí",font = ("Open Sans",15))
        self.descripcion_filtro = tk.Label(self,text = "filtrado por hora", font = ("Open Sans",15))
        
        
        self.titulo.grid(row=0,columnspan=3)
        self.descripcion_nombre.grid(row=3,column=0)
        self.descripcion_artista.grid(row=3,column=1)
        self.descripcion_genero.grid(row=3,column=2)
        self.descripcion_entry.grid(row=1,columnspan = 3)
        self.descripcion_filtro.grid(row=5)
        
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=80,font=("Open Sans",15))
        
        self.filtrado = None
        
        self.texto = tk.Entry(self)
        self.texto.grid(pady = 5, row = 2,columnspan=3,)
        texto = self.texto.get()
        
        self.filtrado_hora = tk.Listbox(self)
        self.filtrado_hora.bind("<Double-Button-1>",self.filtrar_eventos_hora(texto))
        
        self.listbox.bind("<Double-Button-1>",self.seleccionar_evento)
        
        self.filtrado_hora.grid(row = 6)
        self.listbox.grid(pady=10,row=6,column=1)
        
        
        
        self.boton_nombre = tk.Button(
            self,
            text="Busca por nombre",
            command = lambda : [self.actualizar_eventos_nombre(self.texto.get()),self.filtrar_eventos_nombre_hora(self.texto.get())],
        )
        self.boton_artista = tk.Button(
            self,
            text="Busca por artista",
            command = lambda : [self.actualizar_eventos_artista(self.texto.get()),self.filtrar_eventos_artista_hora(self.texto.get())],
        )
        self.boton_genero = tk.Button(
            self,
            text="busca por genero",
            command = lambda : [self.actualizar_eventos_genero(self.texto.get()),self.filtrar_eventos_genero_hora(self.texto.get())],
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
        self.boton_filtra_hora = tk.Button(
            self,
            text = "filtrar por hora",
        )
        
        self.boton_nombre.grid(pady = 5,row=4,column=0)
        self.boton_artista.grid(pady = 5,row=4,column=1)
        self.boton_genero.grid(pady = 5,row=4,column=2)
        self.boton_volver.grid(row=7,column=0)
        self.boton_inicio.grid(row=7,column=2)
        
    def actualizar_eventos_nombre(self,nombre):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador.
        """
        self.bandera = "nombre"
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
        self.bandera = "artista"
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
        self.bandera = "genero"
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
    
    def obtener_filtro_hora_seleccionado(self):
        
        indice = self.filtrado_hora.curselection()
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
        
    def seleccionar_filtro(self,event):
        self.controlador.seleccionar_filtro()
    
    def filtrar_eventos_nombre_hora(self,nombre):
        eventos = self.controlador.filtrar_eventos_nombre_hora(nombre)
        self.filtrado = eventos
        self.filtrado_hora.delete(0, tk.END)
        for evento in eventos:
            self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
    
    def filtrar_eventos_artista_hora(self,artista):
        eventos = self.controlador.filtrar_eventos_nombre_hora(artista)
        self.filtrado = eventos
        self.filtrado_hora.delete(0, tk.END)
        for evento in eventos:
            self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
    
    def filtrar_eventos_genero_hora(self,genero):
        eventos = self.controlador.filtrar_eventos_nombre_hora(genero)
        self.filtrado = eventos
        self.filtrado_hora.delete(0, tk.END)
        for evento in eventos:
            self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
    
    def filtrar_eventos_hora(self,event,texto):
        indice = self.obtener_filtro_hora_seleccionado()
        if self.bandera == "nombre":
            eventos = self.controlador.filtrar_hora_nombre(self.filtrado[indice].hora_inicio,"mateos",texto)
            self.listbox.delete(0, tk.END)
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        # elif self.bandera == "artista":
            
            
            
            