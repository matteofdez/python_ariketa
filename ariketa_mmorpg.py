import re
log = "[12:30] PlayerA hit Dragon for 345 damage"
patron = r"\[\d{2}:\d{2}\] (\w+) hit (\w+) for (\d+) damage"
resultado = re.search(patron, log)
if resultado:
    jugador = resultado.group(1)
    enemigo = resultado.group(2)
    dano = resultado.group(3)
    print("Jugador:", jugador)
    print("Enemigo:", enemigo)
    print("Daño:", dano)