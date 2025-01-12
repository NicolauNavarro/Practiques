"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 4
Taula de multiplicar
"""

size = 10

print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end=" ")
print()
print("    " + "-" * (size * 5))

for row in range(1, size + 1):
    print(f"{row:2} |", end=" ")
    for i in range(1, size + 1):
        print(f"{row * i:4}", end=" ")
    print()

