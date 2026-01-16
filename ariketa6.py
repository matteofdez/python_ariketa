print('Ejercicio 6: Función para invertir una cadena' \
'Crea invertir_cadena(cadena) que devuelva la cadena invertida.')
def invertir_cadena(cadena):
    return cadena[::-1]
texto = input("Introduce una cadena de texto: ")
invertida = invertir_cadena(texto)
print(f"Invertido es: {invertida}")