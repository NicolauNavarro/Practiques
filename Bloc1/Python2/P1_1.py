"""
    Practica 1.1, Salutació
    Nicolau Navarro Arroyo
"""

name = ""
while name == "":
    name = input("ingresa el teu nom: ").strip()

print("Benvingut " + str(name.capitalize()))
