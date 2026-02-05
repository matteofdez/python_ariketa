import re

texto = 'u<Skill name="Fireball" cooldown="12s" damage="80">'

patron = re.compile(
    r'u<Skill\s+name="(?P<name>[^"]+)"\s+cooldown="(?P<cooldown>[^"]+)"\s+damage="(?P<damage>[^"]+)">'
)

m = patron.search(texto)
if m:
    print("Nombre:", m.group("name"))
    print("Cooldown:", m.group("cooldown"))
    print("Daño:", m.group("damage"))
