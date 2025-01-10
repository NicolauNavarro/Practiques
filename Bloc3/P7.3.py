

side = int(input("Lado: "))

row = side

space = int((side * 2 + side - 2 - row)/2)

print(" "*space, "*"*side)
for i in range(1, side*2 - 1):
    if i < side :
        row = row + 2
    else:
        row = row - 2
    space = int((side * 2 + side - 2 - row)/2)
    print(" "*space, "*"*row)


