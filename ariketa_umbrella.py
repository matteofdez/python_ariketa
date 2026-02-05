def vigenere_procesar(texto, clave, modo):
    texto_upper = texto.upper()
    clave_lista = preparar_clave(clave, texto_upper)
    
    resultado = []
    for i, char in enumerate(texto_upper):
        if char.isalpha():
            k_char = clave_lista[i]
            shift = ord(k_char) - ord('A')
            if modo == 'cifrar':
                nuevo = (ord(char) - ord('A') + shift) % 26 + ord('A')
            else:
                nuevo = (ord(char) - ord('A') - shift) % 26 + ord('A')
            resultado.append(chr(nuevo))
        else:
            resultado.append(char)
    return ''.join(resultado)

def preparar_clave(clave, texto):
    clave_limpia = clave.upper()
    clave_lista = []
    j = 0
    for char in texto:
        if char.isalpha():
            clave_lista.append(clave_limpia[j % len(clave_limpia)])
            j += 1
        else:
            clave_lista.append(None)
    return clave_lista

# Uso interactivo
texto = input("Ingresa el mensaje: ")
clave = input("Ingresa la clave (ej: UMBRELLA): ")
modo = input("Modo (cifrar/descifrar): ")

resultado = vigenere_procesar(texto, clave, modo)
print("Resultado:", resultado)
