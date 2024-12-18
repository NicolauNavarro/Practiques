"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 2
Any de traspàs
"""

year = int(input("Ingressa un any: "))

leap_year = False
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    if year < 1582:
        leap_year = True
elif year % 4 == 0:
    leap_year = True
        
if leap_year:
    print(str(year) + " és any de traspàs")
else:
    print(str(year) + " no és any de traspàs")

