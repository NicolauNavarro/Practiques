"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 5
Nombre invertit
"""

valid = False
while not valid:
    value = input("Ingresa un nombre: ")
    try:
        value = int(value)
        valid = True
        value = str(value)
    except:
        print("No és un nombre.")

print(value[::-1])

