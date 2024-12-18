"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 10
Triangles
"""

a = float(input("Catet a: "))
b = float(input("Catet b: "))
c = float(input("Catet c: "))

if a > (b + c) or b > (a + c) or c > (a + b):
    print("No és un triangle valid.")
else:
    if a == b:
        if a == c:
            print("El triangle és Equilater.")
        else:
            print("El triangle és Isoceles.")
    elif b == c:
        print("El triangle és Isoceles.")
    elif c == a:
        print("El triangle és Isoceles.")
    else:
        print("El triangle és Escalè.")

