import math
print('Ejercicio 2: Función para calcular el área de un círculo' \
'Crea una función area_circulo (radio) que calcule el área usando la fórmula:' \
'Área = π*radio^2')
def area_circulo(radio):
    return math.pi * (radio ** 2)
r = float(input("Introduce el radio: "))
area = area_circulo(r)
print(f"El área del círculo de radio {r} es {area}")