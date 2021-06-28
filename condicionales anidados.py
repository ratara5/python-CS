p=input ("¿Trabajas desde casa? (si o no)")
if p=="si":
    print ("Que bien!")

else: # o if p=="no", esto se usaría si hubiera más posibles respuestas para la primera consulta
    print ("Trabajas fuera de casa")
    tiempo=int(input("¿Cuántos minutos tardas hasta el trabajo? (Un número entero)"))
    if tiempo==0:
        print ("Trabajas desde casa")
    elif tiempo <=20:
        print ("Llegas rápido")
    elif tiempo>=21 and tiempo<=45:
        print ("Estás en el promedio. Disfruta del paisaje")
    else:
        print ("Aprovecha para leer y escuchar buena música. Disfruta del paisaje")
