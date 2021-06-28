F=3.141516
# Calcular el area de un cuadrado dado su lado
def areacuadrado ():
    l=float(input ("Escribe el valor del lado del cuadrado (decimal usa .) "))
    c=float(l*l)
    print ("El área del cuadrado es "+str(c)+" u^2")

# Calcular el area de un triángulo dados su base y altura
def areatriangulo ():
    b=float(input ("Escribe el valor de la base del triángulo (decimal usa .) "))
    h=float(input("Escribe el valor de la altura del triángulo (decimal usa .) "))
    t=b*h/2
    print("El área del cuadrado es " + str(t) + " u^2")

# Calcular el area de un círculo dado su radio
def areacirculo ():
    r=float(input ("Escribe el valor del radio del circulo (decimal usa .) "))
    c=F*r*r
    print ("El área del cuadrado es "+str(c)+" u^2")

i=True
while i==True:
    s=input("\nEl area de qué figura deseas calcular:\n1. Cuadrado\n2. Triángulo\n3. Círculo\n")
    if s=="1":
        areacuadrado()
    elif s=="2":
        areatriangulo()
    elif s=="3":
        areacirculo()
    else:
        print("Parámetro ingresado no es válido\n")
    c=input("¿Deseas hacer un nuevo cálculo (si o no)\n")
    if c=="si":
        i=True
    else:
        i=False