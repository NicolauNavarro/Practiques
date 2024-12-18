"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 4
Conversió d'unitats
"""

valid = False
while not valid:
    value = input("Longitut en cm: ").replace(",", ".")
    try:
        value = float(value)
        valid = True
    except:
        valid = False

if value == int(value):
    value = int(value)

inch = 2.54
result = round(value / inch, 4)
print(str(value) + " cm = " + str(result) + " in" )

