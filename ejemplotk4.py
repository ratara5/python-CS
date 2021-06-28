#ver ejemplotk1.py para saber qué significan las lineas de este código
from tkinter import *

class Interfaz:
    def __init__(self,contenedor):
        colors = ["black", "white", "gray", "yellow", "blue", "red"]
        self.e1=Label(contenedor, text="Etiqueta1", fg=colors[0], bg=colors[-1])
        self.e1.place(x=20, y=30, width=120, height=25) #administrador place: ubicar elementos en determinadas coordenadas

ventana=Tk()
minterfaz=Interfaz(ventana)
ventana.mainloop()