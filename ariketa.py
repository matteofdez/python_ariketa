
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

'''Ejercicio 2: Función para calcular el área de un círculo
Crea una función area_circulo (radio) que calcule el área usando la fórmula:
Área = π*radio^2
 '''