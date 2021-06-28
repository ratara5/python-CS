
from tkinter import * #importar biblioteca tkinter

class Interfaz: #crear clase interfaz...con clases y métodos de la biblioteca importada...
    def __init__(self,contenedor): #contenedor es el espacio de la ventana pa poner objetos(?)
        self.e1=Label(contenedor, text="Eiqueta1", fg="black", bg="white") #...como la clase Label. e1 es una instancia de la clase Label...
        #...la clase Label debe ser de la biblioteca tkinter.
        self.e1.pack() #pack() es un método de qué clase? de la biblioteca tkinter y acá se le está aplicando a e1


ventana=Tk() #...objeto llamado ventana de la clase Tk(). ventana es una instancia de la clase Inferfaz
minterfaz=Interfaz(ventana) #objeto llamado minterfaz de la clase Interfaz. minterfaz es una instancia de la clase Interfaz
ventana.mainloop() #método aplicado al objeto ventana. Debe ser un método de la clase Tk() (?)