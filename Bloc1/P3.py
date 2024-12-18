"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 3 (Desenvolupada)
Mitjana
"""

import os
import platform

def clear_console():
    system = platform.system()
    if system == "Windows" :
        os.system("clr")
    else:
        os.system("clear")
    print("Practica 1.3: Mitjana")
    print("Nicolau Navarro Arroyo")

clear_console()
print(" ")
print('Escriu "Acabar" en qualsevol moment per sortir.')

def print_results(marks:list):
    clear_console()
    print(" ")
    
    marksSum = 0
    index = 1
    for mark in marks:
        print("Nota " + str(index) + ": " + str(mark).replace(".", ","))
        index = index + 1
        marksSum = marksSum + float(mark)
        
    average = round(marksSum / len(marks), 2)
    if average == int(average):
        average = int(average)
        
    print(" ")
    print("Mitjana: " + str(average).replace(".", ","))
    

marks = []
while True:
    new_mark = input("Insereix una nota: ").strip().replace(",", ".")
    if new_mark == "Acabar":
        break
    
    try:
        float(new_mark)
        marks.append(new_mark)
        print_results(marks)
    except:
        print("El valor no és valid")
    
