import ariketa3
print('Ejercicio 4: Función para encontrar el mayor de tres números' \
'Escribe mayor_de_tres(a, b, c) que devuelva el número más grande' \
'Define es_par(numero) que devuelva True si el número es par y False si es impar.' \
'Los números se deben de obtener por teclado')
def mayor_de_tres(a, b, c):
    return  max(a, b, c)
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num_mayor=mayor_de_tres(num1,num2,num3)
print(f"El numero mas grande es {num_mayor}")
ariketa3.es_par(num1)
ariketa3.es_par(num2)
ariketa3.es_par(num3)
