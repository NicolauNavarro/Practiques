"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 5.1
Ordenament amb ifs
"""

num_1 = float(input("Ingresa un numero: ").replace(",", "."))
num_2 = float(input("Ingresa un numero: ").replace(",", "."))

## Treure decimals inecesaris (Decoratiu)
def rmvDecimals(num):
    if num == int(num):
        return int(num)
    return(num)
num_1 = rmvDecimals(num_1)
num_2 = rmvDecimals(num_2)

if num_1 < num_2:
    print(str(num_1) + " " + str(num_2))
else:
    print(str(num_2) + " " + str(num_1))

