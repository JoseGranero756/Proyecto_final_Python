class ControladorBuscaFiltra:
    def __init__(self,app):
        self.app = app
        
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
    
    def busca(self):
        self.app.cambiar_frame(self.app.vista_busca)
    
    def filtra(self):
        self.app.cambiar_frame(self.app.vista_filtra)