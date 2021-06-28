class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} tiene {} años".format(self.nombre, self.edad)


personas = [
    Persona("Juan", 4),
    Persona("Sebastian", 29),
    Persona("Melissa", 2),
    Persona("Esteban", 14)

]

menores = filter(lambda persona: persona.edad < 18, personas)
for menor in menores:
    print(menor)