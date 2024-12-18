"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 4
Paraula més llarga
"""

word_1 = input("Paraula 1: ").strip()
word_2 = input("Paraula 2: ").strip()
len1 = len(word_1)
len2 = len(word_2)

if len1 == len2:
    print("Les dues paraules són igual de llargues.")  
elif len1 > len2:
    print("La paraula " + word_1 + " és " + str(len1 -  len2) + " lletres més llarga que " + word_2 + ".")
else:
    print("La paraula " + word_2 + " és " + str(len2 -  len1) + " lletres més llarga que " + word_1 + ".")

