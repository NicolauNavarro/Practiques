"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 2
Cercles
"""

import math
pi = math.pi

valid = False
while not valid:
    radius = input("Ingressa el Radi: ").replace(",", ".")
    try:
        radius = float(radius)
        valid = True
    except:
        valid = False

perimeter = 2 * pi * radius
area = pi * radius ** 2

print("Perimetre: " + str(round(perimeter, 2)) )
print("Ârea: " + str(round(area, 2)) )

