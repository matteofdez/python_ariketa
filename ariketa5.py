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
