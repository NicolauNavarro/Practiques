"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 7.3
Dibuixos d'asteriscs
"""

side = int(input("Lado: "))
row = side

for i in range(1, side*2):
    space = int((side * 3 - 2 - row)/2)
    print(" "*space, "*"*row)
    if i < side :
        row = row + 2
    else:
        row = row - 2

