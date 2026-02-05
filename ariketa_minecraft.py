coordenadas = "(x=123, y=-42, z=87)"
cadena = coordenadas.strip("(): ")
cords = cadena.split(", ")
# Se crea un diccionario
diccionario = {}
for cor in cords:
    #Divide entre la clave (xyz) y valor (numero)
    clave, valor = cor.split("=")  
    #Añade al diccionario
    diccionario[clave] = int(valor)
print(diccionario)