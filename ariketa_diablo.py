texto = "Sword(ATK+12), Shield(DEF+8), Potion(HP+50)"

objetos = texto.split(", ")
diccionario = {}

for obj in objetos:
    nombre, resto = obj.split("(")     
    atributo, valor = resto[:-1].split("+")
    diccionario[nombre] = {atributo: int(valor)}
print(diccionario)