#ver ejemplotk1.py para saber qué significan las lineas de este código
from tkinter import *

class Interfaz:
    def __init__(self,contenedor):
        self.e1=Label(contenedor, text="Etiqueta1", fg="black", bg="white")
        self.e2=Label(contenedor, text="Etiqueta2", fg="black", bg="blue")
        self.e3=Label(contenedor, text="Etiqueta3", fg="black", bg="gray" )
        self.e1.pack(side=TOP) #administrador de contenido pack (o método): Agrega uno tras otro
        self.e2.pack(side=RIGHT)
        self.e3.pack(side=BOTTOM,fill=X)

ventana=Tk()
minterfaz=Interfaz(ventana)
ventana.mainloop()
