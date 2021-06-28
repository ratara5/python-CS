# usar persona como clase abstracta...
from abc import ABCMeta, abstractmethod
# método constructor de Persona
class Persona:
    __metaclass__=ABCMeta #... usar persona como clase abstracta...
    def __init__ (self, edad, nombre, ecivil):
        self.edad=edad
        self.nombre=nombre
        self.ecivil=ecivil
        print ("Se ha creado a la persona de nombre "+self.nombre+", de "+str(self.edad)+" años de edad y estado civil: "+ecivil)

# método hablar de Persona
    @abstractmethod #... usar persona como clase abstracta...
    def hablar(self,*palabras):pass #... indicar que es un método abstracto. Usar persona como clase abstracta...mover a class Deportista
        #for frase in palabras:     #...usar como método abstracto: mover a class Deportista
            #print(self.nombre+": "+frase) #...usar como método abstracto: mover a class Deportista

# método constructor de Deportista: esta es sobreescritura, pues se añade deporte.
# Si no tuviera que añadirse el atributo deporte, no se necesitaría nada más hasta el siguiente def
class Deportista(Persona): #...Final: La clase  Persona al derivarse de una clase abstracta Persona, pasa a denominarse implementación
    def __init__ (self, edad, nombre, ecivil, deporte):
        self.edad = edad
        self.nombre = nombre
        self.ecivil = ecivil
        self.__deporte = deporte
        print("Se ha creado a la persona de nombre " + self.nombre + ", de " + str(
            self.edad) + " años de edad y estado civil: " + ecivil+", que practica "+deporte)

    def practicardeporte(self):
        print(self.nombre+": Voy a practicar")

    def vermideporte(self):
        return self.__deporte

    def hablar(self,*palabras):    #...usar como método abstracto: movido desde class Persona
        for frase in palabras:     #...usar como método abstracto: movido desde class Persona
            print(self.nombre+": "+frase) #...usar como método abstracto: movido desde class Persona


# Luis que ahora es una instancia Deportista, sigue comportándose como una instancia de Persona,
# porque ha heredado sus métodos.

luis=Deportista(30, "Luis", "soltero","natación") #ya acepta 4 parámetros por que el constructor de persona está sobreescrito
#print ("Luis practica "+luis.__deporte) #no va a funcionar pues es atributo privado
print ("Luis practica "+luis.vermideporte()) #para mostrar atributo oculto, se llama al método público que lo retorna
luis.hablar("Hola, estoy hablando", "Este soy yo", "Hay alguien ahí?") #método hablar sigue siendo el mismo heredado de persona
luis.practicardeporte()

