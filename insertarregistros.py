#Esta función permite insertar registros en la tabla "tabla" de la base...
#...de datos "novelas.db"
import sqlite3

def insertar():

    db1=sqlite3.connect("novelas.db") #método connect para crear el enlace a la bd
    print ("estás en la función insertar")

    nombre1=input("Escribe el título de la novela")
    autor1=input("Escribe el autor de la novela")
    year1=str(input("Digita el año de la novela"))

    consulta=db1.cursor() #Habilita conexión con el método cursor

    strConsulta="insert into tabla(nombre, autor, year) values ('"+nombre1+"','"+autor1+"','"+year1+"')" #En una variable se asignan a las columnas las entradas correspondientes
    print(strConsulta)
    consulta.execute(strConsulta) #Permitirá consultar los registros de la tabla./Ejecuta el...
    ...#comando llamado strConsulta (?)
    consulta.close() #cerrar consulta
    db1.commit() #guardar cambios
    db1.close() #cerrar base de datos

insertar()
