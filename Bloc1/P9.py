"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 9
Nota necessària
"""

c1 = float(input("Nota certamen 1 (0-100): ")) 
c2 = float(input("Nota certamen 2 (0-100): ")) 
l = float(input("Nota Laboratori (0-100): "))
needed_mark = 60

c3 = (3 * needed_mark - 0.9 * l)/0.7 - c1 - c2
print("Necesites un " + str(round(c3, 2)) + " en el certamen 3")

