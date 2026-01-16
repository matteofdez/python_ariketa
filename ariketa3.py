print('Ejercicio 3: Función para determinar si un número es par o impar' \
'Define es_par(numero) que devuelva True si el número es par y False si es impar.' \
'Los números se deben de obtener por teclado')
def es_par(numero):
    if numero%2==0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
print('Introduce un número para ver si es par o no = ', end='')
numero=int(input())
es_par(numero)