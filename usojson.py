import json

jsonSTR='{"usuarios":[{"nombre":"Mario","status":"online"},{"nombre":"Jesús","status":"offline"}],"cuentaUsuarios":2}'
jsonDecod=json.loads(jsonSTR)

print(jsonDecod) #muestra el objeto jsonSTR (es un diccionario con dos elementos, uno de ellos es una lista, que a su vez tiene dos elemento
# tipo diccionario, y el otro es un número
print(jsonDecod["usuarios"]) #busca la propiedad usuario y la muestra (es una lista con dos elementos tipo diccionario)
print(jsonDecod["cuentaUsuarios"]) #busca la propiedad cuentaUsuarios y la muestra (es un único valor)
print(jsonDecod["usuarios"][1]["status"]) #busca la propiedad status del elemento 1 de la propiedad usuarios (es un único valor)

usuarios=jsonDecod["usuarios"]
for usuario in usuarios:
    print(str(usuario["nombre"])+": "+str(usuario["status"]))

