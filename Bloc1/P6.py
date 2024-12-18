"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 6
Pitàgores
"""

a = float(input("Ingressa el catet a: ").replace(",", "."))
b = float(input("Ingressa el catet b: ").replace(",", "."))
c = round((a**2 + b**2)**0.5, 2)

if c == int(c):
    c = int(c)

print("La hipotenusa és " + str(c).replace(".", ","))

