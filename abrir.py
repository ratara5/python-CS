#Esta función permite imprimir todos los registros de la tabla "tabla" que se encuentra
#...en la base de datos "novelas.db"

# Importa el módulo sqlite3
import sqlite3

# Crea un objeto de conexión a la base de datos SQLite
con = sqlite3.connect("novelas.db")

# Con la conexión, crea un objeto cursor
cur = con.cursor()

# El resultado de "cursor.execute" puede ser iterado por fila
for row in cur.execute('SELECT * FROM tabla'):
    print(row)

# No te olvides de cerrar la conexión
con.close()