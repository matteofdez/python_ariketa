import math;

print('Ejercicio 1: Función para sumar dos números' \
'Escribe una función sumar(a, b) que reciba dos números y devuelva su suma.' \
'Los números se deben de obtener por teclado')
suma=0
def sumar():
    print('Introduce un número = ', end='')
    numero1 = input() 
    print('Introduce otro número = ', end='')
    numero2 = input()

    #Como Python entiende que es un String, concatena los caracteres, para ello, se parsea con int()
    suma=int(numero1)+int(numero2)
    return suma
print(f'La suma es {sumar()}')

print('Ejercicio 2: Función para calcular el área de un círculo' \
'Crea una función area_circulo (radio) que calcule el área usando la fórmula:' \
'Área = π*radio^2')
def area_circulo(radio):
    return math.pi * (radio ** 2)
r = float(input("Introduce el radio: "))
area = area_circulo(r)
print(f"El área del círculo de radio {r} es {area}")

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
es_par(num1)
es_par(num2)
es_par(num3)

print('Ejercicio 5: Función para generar una lista de números pares hasta N ' \
'Crea numeros_par(n) que devuelva una lista con todos los números pares desde 0 hasta n.' \
'n se deben de obtener por teclado')
def numeros_par(n):
    pares = []
    i = 0
    print(f"Numeros pares hasta N: ")
    while i <= n:
        pares.append(i)
        print(f"{i}") 
        #Se hace mas dos por que son PARES
        i += 2
    return pares
n = int(input("Introduce el valor de n: "))
numeros_par(n)

print('Ejercicio 6: Función para invertir una cadena' \
'Crea invertir_cadena(cadena) que devuelva la cadena invertida.')
def invertir_cadena(cadena):
    return cadena[::-1]
texto = input("Introduce una cadena de texto: ")
invertida = invertir_cadena(texto)
print(f"La cadena invertida es: {invertida}")









