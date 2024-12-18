"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 8
Part decimal
"""

valid = False
while not valid:
    value = input("Ingressa un valor: ").replace(",", ".")
    try:
        value = float(value)
        valid = True
        value = abs(value)
    except:
        valid = False

decimal = round(value - int(value),5)
print(str(decimal).replace(".", ","))

