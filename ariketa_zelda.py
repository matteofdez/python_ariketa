#Pido que introduzcan una frase
print('Introduce una frase= ', end='')
frase = input() 
#Lo separo por espacio
palabras = frase.split()
nombres = []
for palabra in palabras:
    #Si la palabra empieza por mayuscula, se mete en el array nombres
    if palabra[0].isupper():
        nombres.append(palabra)
#Se saca por pantalla cuando ya ha recorrido todo el array
print('Nombres propios:', nombres)
