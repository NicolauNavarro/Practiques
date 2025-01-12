"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 2
Potencies de dos
"""

num = int(input("Ingresa numero: "))

res = []
for i in range(0, num + 1):
    value = str(2 ** i)
    res.append(value)

print(" ".join(res))

