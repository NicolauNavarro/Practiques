"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 3
Divisió
"""

dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

print(" ")
result = dividend / divisor
rest = dividend % divisor
if rest == 0:
    print("La divisió és exacte.")
    quotient = round(result)
else:
    print("La divisió no és exacte.")
    quotient = round(result - (rest / divisor))

print("Quocient: " + str(quotient))
print("Residu: " + str(rest))

