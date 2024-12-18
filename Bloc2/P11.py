"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 11
Índex de massa corporal
"""

height = float(input("Altura en cm: "))
height = height / 100
weight = float(input("Massa en kg: "))
age = float(input("Edat: "))

if (weight / (height**2)) < 22:
    if age < 45:
        print("Condició de risc: Baix")
    else:
        print("Condició de risc: Mitjà")
else:
    if age < 45:
        print("Condició de risc: Mitjà")
    else:
        print("Condició de risc: Alt")

