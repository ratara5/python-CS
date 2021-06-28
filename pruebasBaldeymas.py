##### LOS BALDES #####
# Esta función permite saber cuántas veces aparece un número aleatorio de una lista en un intervalo

#lista de n valores aleatorios
import random

def listaAleatorios(n):
    s=[0]*n
    for i in range(n):
        s[i]=round(random.random(),2) # a medida que aumenta las cifras significativas, la distribución en intervalos es más pareja
    return s #necesario hacer el return(?)

#valores en intervalo: determina para cada elemento e de la lista dada, si este está en un intervalo dado
def valorEnIntervalo (equis,min,max):
    cuenta=0
    for e in equis: #se recorre la lista
        if min <= e and e< max:
            cuenta = cuenta + 1 #se consolidan las veces que el elemento está en el intervalo
    print("Hay " + str(cuenta) + " elementos de la lista en el intervalo (" + str(min) + "," + str(max) + ")")

#generar intervalos y decir cuántos números de la lista están en cada intervalo
def finalIntervalo(cantaleat,cantbald):
    x=listaAleatorios(cantaleat)
    interv = 1 / cantbald
    for j in range(cantbald):
        a = j * interv #se genera el min del intervalo
        b = a + interv #se genera el max del intervalo
        valorEnIntervalo(x, a, b)

finalIntervalo(1000,8)