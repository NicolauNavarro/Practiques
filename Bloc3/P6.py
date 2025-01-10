


total = 0
while True:
    new = int(input("Duració tram: "))
    if new == 0 :
        break
    total = total + new

horas = 0
while total >= 60:
    total = total - 60
    horas = horas + 1

print("El temps total del viatge es de: " + str(horas)  + ":" + str(total) + " Horas")


