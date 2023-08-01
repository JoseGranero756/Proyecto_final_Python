class ControladorInicio:
    """
    Cambia el frame a la vista correspondiente dependiendo del botón usado en vista_inicio
    """
    def __init__(self,app): 
        self.app = app
        
    def mostrar_eventos(self ):
        self.app.cambiar_frame(self.app.vista_eventos) # Cambia el frame al que muestra todos los eventos.
    
    def mostrar_asistidos(self):
        self.app.cambiar_frame(self.app.vista_eventos_asistidos) # Cambia el frame al que muestra los eventos asistidos por el usuario cargado.
        
    def mostrar_busca_filtra(self):
        self.app.cambiar_frame(self.app.vista_busca) # Cambia el frame al de busqueda_filtrado.
    