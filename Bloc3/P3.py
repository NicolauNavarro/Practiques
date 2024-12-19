"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 3
Suma entre números
"""

num_1 = int(input("Igresa primer numero: "))
num_2 = int(input("Igresa segon numero: "))

result = 0
for i in range(num_1+1, num_2):
    result = result + i
print("La suma és: " + str(result))

