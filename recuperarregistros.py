#Esta función permite recuperar todos los registros de la tabla "tabla" que se encuentra
#...en la base de datos "novelas.db"

import sqlite3
def consultar():
    db2=sqlite3.connect("novelas.db")
    print ("Estás en la función de consultar") #(¿)
    db2.row_factory=sqlite3.Row #método row_factory para preparar la consulta
    consulta=db2.cursor() #habilita la consulta
    consulta.execute("select * from tabla")
    filas=consulta.fetchall() #método fetchall pa guardar el resultado de la consulta
    lista=[]
    for fila in filas:
        s={}
        s['nombre']=fila['nombre']
        s['autor']=fila['autor']
        s['year']=str(fila['year'])
        lista.append(s) #¿Es una lista o un diccionario? ¿O una lista con elementos diccionario?
    consulta.close()
    db2.close()
    return(lista)

ListaNovelas=consultar()
for novela in ListaNovelas: #¿Es una lista o un diccionario? ¿O una lista con elementos diccionario?
	print (novela['nombre'],novela['autor'],novela['year'])

