
## Aquesta practica accepta decimals en forma de "," i els expressa d'igual manera.
## A més a més no "peta" en inserir text en comptes de numeros.
## Utilitza una variable de tipus llista per guradar els resultats previs.

import os
import platform
import math
pi = math.pi


def clear_console():
    system = platform.system()
    if system == "Windows" :
        os.system("clr")
    else:
        os.system("clear")
    print("Practica 1.2: Cercles")
    print("Nicolau Navarro Arroyo")


clear_console()
print(" ")
print('Escriu "Acabar" en qualsevol moment per sortir.')
    
    
def calc_perimeter(radius):
    return round(2 * pi * radius, 2)
    
def calc_area(radius):
    return round(pi * radius ** 2, 2)
    
def print_results(results):
    clear_console()
    print(" ")
    for radius in results:
        radius = float(radius)
        if radius == int(radius):
            radius = int(radius)
        print("Radi:      " + str(radius).replace(".", ","))
        print("Perimetre: " + str(calc_perimeter(radius)).replace(".", ","))
        print("Area:      " + str(calc_area(radius)).replace(".", ","))
        print(" ")


history = []
while True:
    radius = input("Escriu el radi del cercle: ").strip().replace(",", ".")
    if radius == "Acabar":
        break
    try:
        float(radius)
        history.append(radius)
        print_results(history)
    except:
        print("El valor no és valid")
    
    




