# método constructor de Persona
class Persona:
    def __init__ (self, edad, nombre, ecivil):
        self.edad=edad
        self.nombre=nombre
        self.ecivil=ecivil
        print ("Se ha creado a la persona de nombre "+self.nombre+", de "+str(self.edad)+" años de edad y estado civil: "+ecivil)

# método hablar de Persona
    def hablar(self,*palabras):
        for frase in palabras:
            print(self.nombre+": "+frase)

# método constructor de Deportista: esta es sobreescritura, pues se añade deporte.
# Si no tuviera que añadirse el atributo deporte, no se necesitaría nada más hasta el siguiente def
class Deportista(Persona):
    def __init__ (self, edad, nombre, ecivil, deporte):
        self.edad = edad
        self.nombre = nombre
        self.ecivil = ecivil
        self.deporte=deporte
        print("Se ha creado a la persona de nombre " + self.nombre + ", de " + str(
            self.edad) + " años de edad y estado civil: " + ecivil+", que practica "+deporte)
    def practicardeporte(self):
        print(self.nombre+": Voy a practicar")

# Luis que ahora es una instancia Deportista, sigue comportándose como una instancia de Persona,
# porque ha heredado sus métodos.
juan=Persona(20, "Juan", "soltero")
juan.hablar("Hola, estoy hablando", "Este soy yo", "Hay alguien ahí?")
luis=Deportista(30, "Luis", "soltero","natación") #ya acepta 4 parámetros por que el constructor de persona está sobreescrito
print ("Luis practica "+luis.deporte)
luis.hablar("Hola, estoy hablando", "Este soy yo", "Hay alguien ahí?") #método hablar sigue siendo el mismo heredado de persona
luis.practicardeporte()