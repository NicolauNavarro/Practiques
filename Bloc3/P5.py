"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 5
Divisors
"""

num = int(input("Ingresa el numero: "))

res = []
for i in range(1, num + 1):
    if num % i == 0:
        res.append(str(i))

print(" ".join(res))

