"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 1
Número parell
"""

valid = False
while not valid:
    value = input("Ingresa un número parell: ")
    try:
        value = float(value)
        valid = True
    except:
        valid = False

if value % 2 == 0:
    print("El número és parell.")
else:
    print("El número és imparell")

