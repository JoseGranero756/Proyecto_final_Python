import tkinter as tk
from tkinter.font import Font 

class VistaBusca(tk.Frame):
    def __init__(self,master = None, controlador = None):
        """
        Crea la vista de la pantalla de busqueda
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.titulo = tk.Label(self,text = "Busqueda de eventos", font = ("Roboto",20))
        self.titulo.grid(row=0,columnspan=3)
        
        # Bandera para controlar por que categoría se buscó al ultimo
        self.bandera = None 
        
        # Crea las etiquetas de descripción
        self.descripcion_nombre = tk.Label(self,text = "Buscar eventos por nombre",font = ("Open Sans",15))
        self.descripcion_artista = tk.Label(self,text = "Buscar eventos por artista",font = ("Open Sans",15))
        self.descripcion_genero = tk.Label(self,text = "Buscar eventos por genero",font = ("Open Sans",15))
        self.descripcion_entry = tk.Label(self,text = "Buscar escribiendo aquí",font = ("Open Sans",15))
        self.descripcion_filtro = tk.Label(self,text = "filtrado por hora", font = ("Open Sans",15))
        
        self.descripcion_nombre.grid(row=3,column=0)
        self.descripcion_artista.grid(row=3,column=1)
        self.descripcion_genero.grid(row=3,column=2)
        self.descripcion_entry.grid(row=1,columnspan = 3)
        self.descripcion_filtro.grid(row=5)
        
        # Crea la listbox donde se muestran los eventos por nombre, artista y genero.
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=80,font=("Open Sans",15))
        self.listbox.grid(pady=10,row=6,column=1)
        # Asocia el doble click en elementos de la listbox al metodo seleccinar_evento
        self.listbox.bind("<Double-Button-1>",self.seleccionar_evento)
        
         # Crea una listbox pequeña donde se va a ver el contenido para filtrar por hora
        self.filtrado_hora = tk.Listbox(self)
        self.filtrado_hora.grid(row = 6)
        # Asocia el doble click en la listbox al metodo filtrar_eventos_hora
        self.filtrado_hora.bind("<Double-Button-1>",self.filtrar_eventos_hora)
        
        # Crea la variable filtrado, que va a retener los datos de la ultima lista filtrada
        self.filtrado = None
        
        # Crea el el cuadro de entry para la busqueda
        self.texto = tk.Entry(self)
        self.texto.grid(pady = 5, row = 2,columnspan=3,)
        
        # Crea una variable para pasar el resultado del entry a modulos externos
        self.alm_entry = None
        
        # Crea los botones para realizar las busquedas
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
        # Crea el botón para volver al inicio
        self.boton_inicio = tk.Button(
            self,
            text = "Ir al inicio",
            command=self.controlador.regresar_inicio,
        )
        
        self.boton_nombre.grid(pady = 5,row=4,column=0)
        self.boton_artista.grid(pady = 5,row=4,column=1)
        self.boton_genero.grid(pady = 5,row=4,column=2)
        self.boton_inicio.grid(row=7,column=2)
        
    def actualizar_eventos_nombre(self,nombre):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador que coincidan
        con el nombre pasado.
        """
        
        # Almacena el get entry en la variable alm_entry.
        self.alm_entry = nombre
        # Almacena el botón apretado en la variable bandera.
        self.bandera = "nombre"
        
        # Obtiene los eventos coincidentes con el nombre pasado, llamando a la función en el controlador.
        eventos = self.controlador.obtener_eventos_nombre(nombre)
        # Controla de que el retorno de la función sea tipo lista.
        if type(eventos) == list:
            # Borra datos preexistentes en la listbox principal.
            self.listbox.delete(0, tk.END)
            # Carga los datos obtenidos en la listbox principal.
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        else:
            # Si el dato no era tipo lista se toman como mensaje de error y se cargan en la listbox.
            self.listbox.delete(0,tk.END)
            self.listbox.insert(tk.END,f"{eventos}")
    
    def actualizar_eventos_artista(self,artista):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador que coincidan
        con el artista pasado.
        """
        self.alm_entry = artista 
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
        Actualiza la lista de eventos con los eventos obtenidos en controlador que coincidan
        con el genero pasado.
        """
        self.alm_entry = genero
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
        Retorna el indice del evento seleccionado en la listbox principal.
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None
    
    def obtener_filtro_hora_seleccionado(self):
        """
        Retorna el indice del filtro de hora seleccionado en la listbox de filtros
        """
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
    
    def filtrar_eventos_nombre_hora(self,nombre):
        """
        Carga las horas que están dentro de la lista en eventos que coincidan al nombre pasado.
        """
        eventos = self.controlador.filtrar_eventos_nombre_hora(nombre) # Trae los eventos que coinciden con el nombre y sin repetir las horas de inicio,
        self.filtrado = eventos # Guarda la lista, para poder leer luego la posición de uno de sus elementos con doble click en la listbox
        
        # Carga las horas asociadas al nombre en la listbox de filtrado por hora
        self.filtrado_hora.delete(0, tk.END)
        for evento in eventos:
            self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
    
    def filtrar_eventos_artista_hora(self,artista):
        eventos = self.controlador.filtrar_eventos_artista_hora(artista)
        self.filtrado = eventos
        self.filtrado_hora.delete(0, tk.END)
        for evento in eventos:
            self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
    
    def filtrar_eventos_genero_hora(self,genero):
        eventos = self.controlador.filtrar_eventos_genero_hora(genero)
        self.filtrado = eventos
        self.filtrado_hora.delete(0, tk.END)
        for evento in eventos:
            self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
    
    def filtrar_eventos_hora(self,event):
        """
        Trae el indice en el doble click hecho en una hora de la listbox de filtrado por hora
        y muestra los eventos que coinciden con esa hora y la categoría del ultimo botón apretado.
        """
        # Trae el indice del evento marcado en la listbox de filtro por hora.
        indice = self.obtener_filtro_hora_seleccionado() 
        # Controla la categoría de la ultima busqueda realizada.
        if self.bandera == "nombre": 
            # Llama al metodo de filtrado dandole la hora con el indice obtenido en la lista almacenada en self.filtrado y el nombre del entry.get()
            eventos = self.controlador.filtrar_hora_nombre(self.filtrado[indice].hora_inicio,self.alm_entry) 
            # Borra el contenido de la listbox principal
            self.listbox.delete(0, tk.END)
            # Carga los eventos obtenidos en la listbox principal
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        elif self.bandera == "artista":
            eventos = self.controlador.filtrar_hora_artista(self.filtrado[indice].hora_inicio,self.alm_entry)
            self.listbox.delete(0, tk.END)
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        elif self.bandera == "genero":
            eventos = self.controlador.filtrar_hora_genero(self.filtrado[indice].hora_inicio,self.alm_entry)
            self.listbox.delete(0, tk.END)
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
            
            
            