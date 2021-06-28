import facebook
import requests

def ToCSV(lista):
    cadena=""
    for linea in lista:
        cuenta=0
        for stats in linea:
            if (cuenta!=0):
                cadena=cadena+','+str(stats)
            else:
                cadena=cadena+str(stats).replace(",","").replace("\n","")
                cuenta+=1
        cadena=cadena+'\r'
    csv=open("C:\\Users\\TabSan\\Desktop\\Comentarios.csv","w+")
    csv.write(cadena)
    csv.close()

token="EAALEZBRxoZCuwBAD4sZCvtPzylA7WI2F348rdgEtWnLe0HZALc4KiAmpn2f4Y81jGYVCLk9ENQa9EiqvKtn5BtKR6J4JsoCy8qEZBu9DrQ6SeFbAxNsPrIGGyzZCmUbO9kPZABat1gDYGy1a2o1ZCE2A6VJI6VN5IaIDZAA03WM1fIuUbIfquXtGrWhluZADfelXLtSjrb9xJwDwZDZD" # token de facebook
graph=facebook.GraphAPI(token)
cantidadComentarios=100
PageId='147567027115848' #el pageId del usuario?

cuentaLikes=0
cuentaPaginas=0
cuentaComentarios=0
ListaComents=[]

bandera=False

coments=graph.get_connections(PageId,'feed')

print(coments)

while True: # Ciclo infinito
    try:
        for coment in coments['data']: # Recorrer los comentarios que se encuentran en el objeto con la llave de data
            IstComent=[]
            try:
                mensaje=coment['message']
            except KeyError:
                continue # Descartar los objetos que no traen un mensaje, como imágenes o videos
            cuentaLikes=0
            print(mensaje)
            while True:
                try:
                    for like in coments['likes']['data']: # Recorrer los primeros 25 likes del comentario, una vez terminados los 25
                        # se hace el request con el paginado
                        cuentaLikes=cuentaLikes+1
                    coment['likes']=requests.get(coment['likes']['paging']['next']).json()
                except KeyError:
                    break
            print(cuentaLikes)
            IstComent.append(mensaje) # Guarda en un arreglo el mensaje...
            IstComent.append(cuentaLikes) # ...y el total de likes...
            ListaComents.append(IstComent) # ...y lo agrega a la lista de comentarios
            cuentaComentarios=cuentaComentarios+1
            print("")
            if(cuentaComentarios>=cantidadComentarios): # Salir de los bucles cuando se llegue a los 100 comentarios extraídos
                bandera=True
                break
        if (bandera): # Salir de los bucles cuando se llegue a los 100 comentarios extraídos
            break
        coments=requests.get(coments['paging']['next']).json() # Si no se ha llegado a los 100 comentarios extraídos, vuelve a hacer el request
        # con el paginado
    except KeyError:
        break # Salir del bucle si se acaban los comentarios antes de los 100

ToCSV(ListaComents)
print("")
print("Páginas Analizadas: "+str(cuentaPaginas))




