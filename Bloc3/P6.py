"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 6
Temps de viatge
"""

total = 0
while True:
    new = int(input("Duració tram: "))
    if new == 0 :
        break
    total = total + new

hours = 0
while total >= 60:
    total = total - 60
    hours = hours + 1

if total < 10:
    total = "0" + str(total)
else:
    total = str(total)

print("Temps total del viatge: " + str(hours)  + ":" + str(total) + " hores.")

