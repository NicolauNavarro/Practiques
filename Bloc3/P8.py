"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 8
Càlcul de pi pel mètode d'Arquimedes 
"""

import math

a = 1
sides = 3
aprox_pi=3

while (abs(math.pi - aprox_pi) > (10 ** -16)):
    b = (1**2 - (a/2)**2)**0.5
    x = 1 - b
    c = (x**2 + (a/2)**2)**0.5
    a = c
    sides = sides * 2 
    aprox_pi=c*sides
    
print(aprox_pi)

