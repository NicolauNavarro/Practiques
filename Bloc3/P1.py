"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 1
Multiples
"""

num = float(input("Ingresa un numero: ").replace(",", "."))
if num == int(num):
    num = int(num)

for i in range(1, 11):
    result = round(i * num, 2)
    if result == int(result):
        result = int(result)
    print(f'{num} X {i} = {result}')

