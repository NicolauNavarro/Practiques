"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 6
Letra o numero
"""

value = input("Ingresa un caracter: ")

if value.isnumeric():
    print("És un numero")
elif value.isalpha():
    if value.isupper():
        print("Es majuscula")
    else:
        print("Es minusula")
else:
    print("No es ni lletra ni numero")
    
