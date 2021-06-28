# escribir en un archivo nuevo
def escritura(datoa,datob,datoc):
    prueba=open('C:/Users/TabSan/Desktop/datos.py','w')
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print ("\nEscritura\n") #para verificar que se está escribiendo

escritura("Hola"," mundo"," bonito")

#leer un archivo
def lectura():
    prueba=open('C:/Users/TabSan/Desktop/datos.py','r')
    print(prueba.read())
    prueba.close()
lectura()
