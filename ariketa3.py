print('Ejercicio 3: Función para determinar si un número es par o impar' \
'Define es_par(numero) que devuelva True si el número es par y False si es impar.' \
'Los números se deben de obtener por teclado')
#La función para determinar si es par o impar
def es_par(numero):
    #Si el resto es igual a cero es par
    if numero%2==0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
print('Introduce un número para ver si es par o no = ', end='')
numero=int(input())
#Llamada a la función
es_par(numero)