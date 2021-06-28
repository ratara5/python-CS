#Del libro "Aprenda a pensar como un programaador de Python"
#No  hacer salto de linea en python 3.8 https://www.discoduroderoer.es/no-hacer-un-salto-de-linea-en-python-con-print/

def imprimeMultiplosColumnas(m,n): #imprime múltiplos de n en m columnas
    i=1
    while i<=m:
        print (str(n*i)+"\t",end="")
        i=i+1
    print("")

def tablaCuadradafilasMultiplos(q): #q es la última tabla dispuesta en fila
    p = 1 #se pueden usar variables n o m y no hay problema pues son internas
    while p<=q:
        imprimeMultiplosColumnas(q,p) #q,p->tabla cuadrada // p,p->pirámide
        p=p+1

tablaCuadradafilasMultiplos(5)
print("banana"[0]) #imprimir caracter de una cadena directamente ecsrita en print
print(len("banana")) #imprimir longitud de una cadena directamente ecsrita en print

#imprimir invertidos caracteres por linea
i=1
fruta="banana"
while i<=(len(fruta)):
    print(fruta[-i])
    i=i+1
#seleccionar caracteres
s = "Pedro, Pablo, y María"
print (s[7:12]) #ubicarse (contando dede 0) en el comienzo del carácter deseado, sumarle a esa posición la longitud de la 'palabra' deseada: ese será el índice final)

mipalabra="Zapato"
mipalabra=mipalabra.lower() #necesario convertir a minúsculas para efectuar comparación alfabética
if mipalabra>"banana":
    print ("la palabra "+mipalabra+" está alfabéticamente después de (es mayor que '>') banana")

def cuentaLetras(palabra,letra): #función pa contar cuántas veces aparece una letra en una palabra
    cuenta=0
    for caracter in palabra:
        if caracter==letra:
            cuenta=cuenta+1
    print ("la letra "+letra+" está "+str(cuenta)+" veces en la palabra "+palabra)
    return cuenta

cuentaLetras("hermenegilda gil","a")

print("la primera 'a' de la palabra 'banana' está en el índice "+str("banana".find("a")))
print("la primera 'a' de la palabra 'patos' está en el índice "+str("patos".find("a",2,len("patos")-1)))
#busca la letra 'a' entre el índice 2 y el índice 4, la búsqueda arroja "-1" pues falla, ya que no hay ninguna 'a' allí


print(str("PAN".isupper())) #imprime el valor bool que indica si la palabra "PAN" es mayúscula (lower() se usa pa minús)
print(str("n" in "casaca"))  #imprime el valor bool que indica si la letra "n" está en la palabra "casaca"

import string
print(string.ascii_lowercase) #
print(string.ascii_uppercase)
print(string.digits)
print(string.whitespace)

# función para saber la posición de una letra en el abecedario
def posicionLetra(letra):
    print("la letra "+letra+" está en el índice "+str(string.ascii_lowercase.find(letra)))

posicionLetra("d")

# Deben evitarse los alias (es decir, asignar una variable a otra) para objetos mutables...
a=[1,2,3]
print(a)
b=a
b[0]=5
print(a)

#... si se requiere copiar una lista en otra, pero sin afectar el contenido de la primera se hace clonación
a=[1,2,3]
b=[]
b[:]=a[:]
print (a)
b[0]=5
print(a)

#split y join en cadenas y listas
cadena="patos al agua"
lista="patos al agua".split() #split devuelve una lista
print("lista: "+str(lista))
nuevacadena="_".join(lista) #join devuelve una cadena
print(nuevacadena)

#tupla es similar a una lista pero inmutable

print(type(("a",))) # tupla de un elemento: entre PARÉNTESIS, INCLUIR una coma al FINAL

a=(1,2,3,4,5)
b=("a","b","c","d","e")
print(a)
print(b)
a,b=b,a #intercambio de valores entre tuplas. Hacerlo dentro de una función trae errores semánticos
print("\nse produce el intercambio")
print(a)
print(b)

#Números aleatorios
import random
for i in range(5): #entregueme 5 enteros aleatorios...
    aleanum=int((4+1)*round(random.random(),3))
    print(str(aleanum)+"\t",end="") #...entre 0 y 4 incluido el 4
print("\n\n")

#entregueme 1 enteros aleatorio...
menor=4
mayor=9
aleanum=menor+int((mayor+1-menor)*round(random.random(),2))
print(aleanum) #...entre menor y el nueve incluido el mayor

#función que hace lo anterior siendo b el nummayor y a el nummenor
def AleatorioEntre (a,b):
    print("El aleatorio entre "+str(a)+" y "+str(b)+" es: "+str(a+int((b+1-a)*round(random.random(),2))))

AleatorioEntre(2,7)


listaAleatorios(8)
print(s)




