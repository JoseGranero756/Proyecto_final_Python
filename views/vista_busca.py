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
        self.lista_eventos = None
        
        # Crea las etiquetas de descripción
        self.descripcion_nombre = tk.Label(self,text = "Buscar eventos por nombre",font = ("Open Sans",15))
        self.descripcion_artista = tk.Label(self,text = "Buscar eventos por artista",font = ("Open Sans",15))
        self.descripcion_genero = tk.Label(self,text = "Buscar eventos por genero",font = ("Open Sans",15))
        self.descripcion_entry = tk.Label(self,text = "Buscar escribiendo aquí",font = ("Open Sans",15))
        self.descripcion_filtro_hora = tk.Label(self,text = "Filtrado por hora", font = ("Open Sans",15))
        self.descripcion_filtro_ubicacion = tk.Label(self,text = "Filtrado por ubicación",font = ("Open Sans",15))
        
        self.descripcion_nombre.grid(row=3,column=0)
        self.descripcion_artista.grid(row=3,column=1)
        self.descripcion_genero.grid(row=3,column=2)
        self.descripcion_entry.grid(row=1,columnspan=3)
        self.descripcion_filtro_hora.grid(row=5,column=0)
        self.descripcion_filtro_ubicacion.grid(row=5,column=2)
        
        
        # Crea la listbox donde se muestran los eventos por nombre, artista y genero.
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=80,font=("Open Sans",15))
        self.listbox.grid(pady=10,row=6,column=1)
        # Asocia el doble click en elementos de la listbox al metodo seleccinar_evento
        self.listbox.bind("<Double-Button-1>",self.seleccionar_evento)
        
         # Crea una listbox pequeña donde se va a ver el contenido para filtrar por hora
        self.filtrado_hora = tk.Listbox(self)
        self.filtrado_hora.grid(row = 6)
        # Asocia el doble click en la listbox filtrado_hora al metodo filtrar_eventos_hora
        self.filtrado_hora.bind("<Double-Button-1>",self.filtrar_eventos_hora)
        
        # Crea una listbox pequeña donde se va a ver el contenido para filtrar por ubicación
        self.filtrado_ubicacion = tk.Listbox(self)
        self.filtrado_ubicacion.grid(row = 6,column = 2)
        # Asocia el doble click en la listbox filtrado_ubicacion al metodo filtrar_eventos_ubicacion
        self.filtrado_ubicacion.bind("<Double-Button-1>",self.filtrar_eventos_ubicacion)
        
        # Crea la variable filtrado, que va a retener los datos de la ultima lista filtrada por hora
        self.eventos_filtrados_hora = None
        # Crea la variable filtrado, que va a retener los datos de la ultima lista filtrada por ubicacion
        self.ubicaciones_filtradas = None
        
        # Crea el el cuadro de entry para la busqueda
        self.texto = tk.Entry(self)
        self.texto.grid(pady = 5, row = 2,columnspan=3,)
        
        # Crea una variable para pasar el resultado del entry a modulos externos
        self.alm_entry = None
        
        # Crea los botones para realizar las busquedas
        self.boton_nombre = tk.Button(
            self,
            text="Busca por nombre",
            command = lambda : self.actualizar_eventos_nombre(self.texto.get()),
        )
        self.boton_artista = tk.Button(
            self,
            text="Busca por artista",
            command = lambda : self.actualizar_eventos_artista(self.texto.get()),
        )
        self.boton_genero = tk.Button(
            self,
            text="busca por genero",
            command = lambda : self.actualizar_eventos_genero(self.texto.get()),
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
        
        # Almacena el entry.get() en la variable alm_entry.
        self.alm_entry = nombre
        
        # Almacena el botón apretado en la variable bandera.
        self.bandera = "nombre"
        
        # Obtiene los eventos coincidentes con el nombre pasado, llamando a la función en el controlador.
        eventos = self.controlador.obtener_eventos_nombre(nombre)
        
        # Controla de que el retorno de la función sea tipo lista.
        if type(eventos) == list:
            self.lista_eventos = eventos
            # Borra datos preexistentes en la listbox principal.
            self.listbox.delete(0, tk.END)
            # Carga los datos obtenidos en la listbox principal.
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        else:
            # Si el dato no era tipo lista se toman como mensaje de error y se cargan en la listbox.
            self.listbox.delete(0,tk.END)
            self.listbox.insert(tk.END,f"{eventos}")
            self.filtrado_ubicacion.delete(0,tk.END)
            
        # obtiene las horas_inicio que coinciden con la lista de eventos del nombre dado sin repetidas.
        self.eventos_filtrados_hora = self.controlador.filtrar_eventos_hora(eventos)
        #controla que el tipo de dato sea lista
        if type(self.eventos_filtrados_hora) == list:
             # Carga las horas asociadas al nombre en la listbox de filtrado por hora
            self.filtrado_hora.delete(0, tk.END)
            for evento in self.eventos_filtrados_hora:
                self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
     
        # obtiene las ubicaciones que coinciden con la lista de eventos del nombre dado sin repetidas.
        self.ubicaciones_filtradas = self.controlador.filtrar_eventos_ubicacion(eventos)
        # Controla que el tipo de dato sea lista
        if type(self.ubicaciones_filtradas) == list:
            # Borra datos preexistentes en la listbox.
            self.filtrado_ubicacion.delete(0, tk.END)
            # Carga los datos en la listbox de filtrado de ubicaciones.
            for ubicacion in self.ubicaciones_filtradas:
                self.filtrado_ubicacion.insert(tk.END,f"{ubicacion.direccion}")
            
    def actualizar_eventos_artista(self,artista):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador que coincidan
        con el artista pasado.
        """
        # Almacena el entry en la variable alm_entry
        self.alm_entry = artista 
        # Almacena la ultima busqueda en la variable bandera
        self.bandera = "artista"
        # Llama al metodo que filtra los artistas en el controlador y almacena la lista filtrada en la variable eventos
        eventos = self.controlador.obtener_eventos_artista(artista)
        # Controla de que sea tipo lista para mostrar el objeto
        if type(eventos) == list:
            self.lista_eventos = eventos
            # Borra el contenido previo de la listbox principal
            self.listbox.delete(0, tk.END)
            # inserta los datos en la listbox principal
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        else:
            # En caso de no ser lista, borra el contenido de la listbox principal si es que tenía antes
            self.listbox.delete(0,tk.END)
            # Inserta el contenido de eventos en la listbox que es un string con mensaje de error para el usuario
            self.listbox.insert(tk.END,f"{eventos}")
            # borra la listbox de ubicación para que su contenido no se vea
            self.filtrado_ubicacion.delete(0,tk.END)
        
        # obtiene las horas_inicio que coinciden con la lista de eventos del artista dado sin repetidas.
        self.eventos_filtrados_hora = self.controlador.filtrar_eventos_hora(eventos)
        #controla que el tipo de dato sea lista
        if type(self.eventos_filtrados_hora) == list:
             # Carga las horas asociadas al nombre en la listbox de filtrado por hora
            self.filtrado_hora.delete(0, tk.END)
            for evento in self.eventos_filtrados_hora:
                self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
            
         # obtiene las ubicaciones que coinciden con la lista de eventos del artista dado sin repetirlas.
        self.ubicaciones_filtradas = self.controlador.filtrar_eventos_ubicacion(eventos)
        # Controla que el tipo de dato sea lista
        if type(self.ubicaciones_filtradas) == list:
            # Borra datos preexistentes en la listbox.
            self.filtrado_ubicacion.delete(0, tk.END)
            # Carga los datos en la listbox de filtrado de ubicaciones.
            for ubicacion in self.ubicaciones_filtradas:
                self.filtrado_ubicacion.insert(tk.END,f"{ubicacion.direccion}")
                            
    def actualizar_eventos_genero(self,genero):
        """
        Actualiza la lista de eventos con los eventos obtenidos en controlador que coincidan
        con el genero pasado.
        """
        # almacena el entry en la variable alm_entry
        self.alm_entry = genero
        # almacena la categoría de la busqueda en bandera
        self.bandera = "genero"
        # Llama al metodo obtener_eventos_genero en controlador y almacena el resultado en la variable eventos
        eventos = self.controlador.obtener_eventos_genero(genero)
        # Controla que el resultado sea tipo lista
        if type(eventos) == list:
            self.lista_eventos = eventos
            # Si es tipo lista
            # Borra datos preexistentes en la listbox principal
            self.listbox.delete(0, tk.END)
            # Carga los datos de eventos en la listbox principal
            for evento in eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        else:
            # si eventos no es una lista
            # Borra el contenido en la listbox princpial
            self.listbox.delete(0,tk.END)
            # Inserta eventos en la listbox que al no ser lista la otra salida de la función es un string con el mensaje de error
            self.listbox.insert(tk.END,f"{eventos}")
            # Borra el contenido de la listbox de ubicación
            self.filtrado_ubicacion.delete(0,tk.END)
            
            # Rellena listbox filtrado por hora
        # obtiene las horas_inicio que coinciden con la lista de eventos del genero dado sin repetidas.
        self.eventos_filtrados_hora = self.controlador.filtrar_eventos_hora(eventos)
        #controla que el tipo de dato sea lista
        if type(self.eventos_filtrados_hora) == list:
             # Carga las horas asociadas al nombre en la listbox de filtrado por hora
            self.filtrado_hora.delete(0, tk.END)
            for evento in self.eventos_filtrados_hora:
                self.filtrado_hora.insert(tk.END,f"hora de inicio: {evento.hora_inicio}")
        
            # Rellena listbox filtrado por ubicación
        # obtiene las ubicaciones que coinciden con la lista de eventos del genero dado sin repetirlas.
        self.ubicaciones_filtradas = self.controlador.filtrar_eventos_ubicacion(eventos)
        # Controla que el tipo de dato sea lista
        if type(self.ubicaciones_filtradas) == list:
            # Borra datos preexistentes en la listbox.
            self.filtrado_ubicacion.delete(0, tk.END)
            # Carga los datos en la listbox de filtrado de ubicaciones.
            for ubicacion in self.ubicaciones_filtradas:
                self.filtrado_ubicacion.insert(tk.END,f"{ubicacion.direccion}")
            
    def obtener_evento_seleccionado(self):
        """
        Retorna el indice del evento seleccionado en la listbox principal.
        """
        indice = self.listbox.curselection()
        if indice and type(self.lista_eventos) == list:
            return self.lista_eventos[indice[0]].id_evento
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
   
    def obtener_filtro_ubicacion_seleccionado(self):
        """
        Retorna el indice del filtro de hora seleccionado en la listbox de filtros
        """
        indice = self.filtrado_ubicacion.curselection()
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
            self.lista_eventos = self.controlador.filtrar_hora_nombre(self.eventos_filtrados_hora[indice].hora_inicio,self.alm_entry) 
            # Borra el contenido de la listbox principal
            self.listbox.delete(0, tk.END)
            # Carga los eventos obtenidos en la listbox principal
            for evento in self.lista_eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        # Si bandera == artista
        elif self.bandera == "artista":
            self.lista_eventos = self.controlador.filtrar_hora_artista(self.eventos_filtrados_hora[indice].hora_inicio,self.alm_entry)
            self.listbox.delete(0, tk.END)
            for evento in self.lista_eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        elif self.bandera == "genero":
            self.lista_eventos = self.controlador.filtrar_hora_genero(self.eventos_filtrados_hora[indice].hora_inicio,self.alm_entry)
            self.listbox.delete(0, tk.END)
            for evento in self.lista_eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
                
    def filtrar_eventos_ubicacion(self,event):
        """
        Trae el indice en el doble click hecho en una hora de la listbox de filtrado por ubicacion
        y muestra los eventos que coinciden con esa ubicación y la categoría del ultimo botón apretado.
        """
        indice = self.obtener_filtro_ubicacion_seleccionado()
        # Controla la categoría de la ultima busqueda realizada.
        if self.bandera == "nombre": 
            # Llama al metodo de filtrado dandole la hora con el indice obtenido en la lista almacenada en self.filtrado y el nombre del entry.get()
            self.lista_eventos = self.controlador.filtrar_ubicacion_nombre(self.ubicaciones_filtradas[indice].id_ubicacion,self.alm_entry) 
            # Borra el contenido de la listbox principal
            self.listbox.delete(0, tk.END)
            # Carga los eventos obtenidos en la listbox principal
            for evento in self.lista_eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        elif self.bandera == "artista":
            self.lista_eventos = self.controlador.filtrar_ubicacion_artista(self.ubicaciones_filtradas[indice].id_ubicacion,self.alm_entry)
            self.listbox.delete(0, tk.END)
            for evento in self.lista_eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        elif self.bandera == "genero":
            self.lista_eventos = self.controlador.filtrar_ubicacion_genero(self.ubicaciones_filtradas[indice].id_ubicacion,self.alm_entry)
            self.listbox.delete(0, tk.END)
            for evento in self.lista_eventos:
                self.listbox.insert(tk.END,f"Nombre: {evento.nombre} Artista: {evento.artista} Genero: {evento.genero}")
        
            
            
            