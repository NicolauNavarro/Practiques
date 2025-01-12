"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 5
Divisors
"""

number = int(input("Ingresa el numero: "))

divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(str(i))

print(f"Els divisors de {number} son: " + ", ".join(divisors))

