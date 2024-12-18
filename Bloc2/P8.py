"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 8
Edat
"""

from time import localtime
t = localtime()

print("Ingresa la teva data de neixament: ")
day = 0
while not (day <= 31 and day > 0):
    day = int(input("Dia: "))

month = 0
while not (month <= 12 and month > 0):
    month = int(input("Mes: "))

year = t.tm_year + 1
while not (year <= t.tm_year):
    year = int(input("Any: "))

yearsPast = t.tm_year - year

if t.tm_mon < month:
    age = yearsPast - 1
elif t.tm_mon == month:
    if t.tm_mday < day:
        age = yearsPast - 1
    else:
        age = yearsPast
    if(day == t.tm_mday):
        print("Felicitats!! Avui és el teu cumple.")
else:
    age = yearsPast
    
print("Tens " + str(age) + " anys")
        
