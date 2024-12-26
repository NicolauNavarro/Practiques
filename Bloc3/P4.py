"""
Nicolau Navarro Arroyo
Bloc 3, Pràctica 4
Suma entre números
"""

size = 50

print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end=" ")
print()
print("    " + "-" * (size * 5))

for i in range(1, size + 1):
    print(f"{i:2} |", end=" ")
    for j in range(1, size + 1):
        print(f"{i * j:4}", end=" ")
    print()

