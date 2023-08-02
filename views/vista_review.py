import tkinter as tk
from tkinter.font import Font
class VistaReview(tk.Frame):
    def __init__(self,master = None, controlador = None):
        """
        Crea la vista de reviews
        """
        
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.evento = None
        
    
        
    def hacer_review(self,evento):
        self.evento = evento
        
    