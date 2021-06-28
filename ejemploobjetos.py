#/ class Persona:
#/    def __init__(self):
#/        self.edad=18
#        self.nombre="Juan"
#        print("Se ha creado a "+self.nombre+" de edad "+str(self.edad))
#    def hablar(self, palabras="No se qué decir"):
#        print (self.nombre+": "+palabras)

#class Persona:
#    def __init__(self,edad="no especificada",nombre="nn"):
#        self.edad=edad
#        self.nombre=nombre
#        print("Se ha creado a "+self.nombre+" de edad "+str(self.edad))
#    def hablar(self, palabras="No se qué decir"):
#        print (self.nombre+": "+palabras)

#juan=Persona(20, "Juan")
#luis=Persona(30,"Luis")
#individuo1=Persona()
#juan.hablar()
#luis.hablar()
#individuo1.hablar()

class Persona:
    def __init__ (self, edad, nombre, ecivil):
        self.edad=edad
        self.nombre=nombre
        self.ecivil=ecivil
        print ("Se ha creado a la persona de nombre "+self.nombre+", de "+str(self.edad)+" años de edad y estado civil: "+ecivil)
    def hablar(self,*palabras):
        for frase in palabras:
            print(self.nombre+": "+frase)

class Deportista(Persona):
    def __init__ (self, edad, nombre, ecivil, deporte): # esta es sobreescritura, pues se añade deporte. Si no estuviera deporte, no se necesitaría nada más hasta el siguiente def
        self.edad = edad
        self.nombre = nombre
        self.ecivil = ecivil
        self.deporte=deporte
        print("Se ha creado a la persona de nombre " + self.nombre + ", de " + str(
            self.edad) + " años de edad y estado civil: " + ecivil+", que practica "+deporte)
    def practicardeporte(self):
        print(self.nombre+": Voy a practicar")


Juan=Persona(20, "Juan", "soltero")
Juan.hablar("Hola, estoy hablando", "Este soy yo", "Hay alguien ahí?")
Luis=Deportista(30, "Luis", "soltero","natación")
Luis.hablar("Hola, estoy hablando", "Este soy yo", "Hay alguien ahí?")
Luis.practicardeporte()

#class Persona:
#    def __init__ (self, edad, nombre, ecivil):
#        self.edad=edad
#        self.nombre=nombre
#        self.ecivil=ecivil
#        print ("Se ha creado a la persona de nombre "+self.nombre+", de "+str(self.edad)+" años de edad y estado civil: "+ecivil)
#    def hablar(self,marcador, **palabras):
#        for frase in palabras:
#            print(self.nombre+": "+marcador+palabras[frase])


#Juan=Persona(20, "Juan", "soltero")
#Juan.hablar("/",t1="Hola, estoy hablando", t2="Este soy yo", t3="Hay alguien ahí?")
#Paco=Persona(27, "Paco", "casado")
#Paco.hablar("/",perro="Hola, estoy hablando", hamster="Este soy yo", gato="Hay alguien ahí?")