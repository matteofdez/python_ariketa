import re
#Pido que introduzcan un RPG
print('Introduce una RPG= ', end='')
rpg=input()
regex = r"^ITEM-\d{4}-(COMMON|RARE|EPIC|LEGENDARY)$"
#Funcion que dice si es válida o no
def validar_item(rpg):
    return bool(re.match(regex, rpg))
esValido=validar_item(rpg)
#Saca por pantalla si es válida o no
print(f'El RPG es {esValido}')

