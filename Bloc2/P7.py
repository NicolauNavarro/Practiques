"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 7
Calculadora
"""

value_1 = float(input("Operando: "))
operation = input("Operador: ").strip()
value_2 = float(input("Operando: "))

if operation == "+":
    result = value_1 + value_2
elif operation == "-":
    result = value_1 - value_2
elif operation == "*":
    result = value_1 * value_2
elif operation == "/":
    result = value_1 / value_2
elif operation == "**":
    result = value_1 ** value_2
else:
    result = "Operadior invalid"

print("El resultat és: " + str(result))

