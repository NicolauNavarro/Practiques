"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 9
Set de tenis
"""

a = int(input("Jocs guanyats per A: "))
b = int(input("Jocs guanyats per B: "))

msg_A = "Guanya A!"
msg_B = "Guanya B!"
msg_I = "Invalid"
msg_c = "Encara continua"

if a > 7 or b > 7:
    print(msg_I)
elif a == 7:
    if b == 6:
        print(msg_A)
    else:
        print(msg_I)
elif b == 7:
    if a == 6:
        print(msg_B)
    else:
        print(msg_I)
elif a == 6:
    if b < 5:
        print(msg_A)
    else:
        print(msg_c)
elif b == 6:
    if a < 5:
        print(msg_B)
    else:
        print(msg_c)
else:
    print(msg_c)
    
