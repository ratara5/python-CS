#Este programa crea la tabla "tabla" en la base de datos "novela.db"
#Crear primero el archivo novela.db

import sqlite3 #importa librería sqlite3

conexion=sqlite3.connect("novelas.db") #crea variable conexión. Con el método connect #objeto llamado conexion de la clase connect?
consulta=conexion.cursor() #Llama método cursor de la variable conexión.

tabla="CREATE TABLE tabla (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
    "nombre VARCHAR (30) NOT NULL,"\
    "autor VARCHAR (40) NOT NULL,"\
    "year INTEGER (9) NOT NULL)"

print (tabla)

if(consulta.execute(tabla)):
	print ("la tabla fue creada")
else:
	print ("la tabla no fue creada")

consulta.close() #deshabilita la conexión
conexion.commit() #método pa guardar los cambios
conexion.close() #cierra la conexión
