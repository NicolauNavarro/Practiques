"""
Nicolau Navarro Arroyo
Bloc 1, Pràctica 7
Hora futura
"""

from datetime import datetime
now = datetime.now()

valid = False
while not valid:
    value = input("Quantitat d'hores: ").replace(",", ".")
    try:
        value = float(value)
        valid = True
    except:
        valid = False


if value == int(value):
    value = int(value)
    
future = now.hour + value
if future >= 24:
    future = future - 24

print("En " + str(value) + " hores seran les " + str(future))

