"""
Nicolau Navarro Arroyo
Bloc 2, Pràctica 5.3
Ordenament amb ifs
"""

num_1 = float(input("Ingresa un numero: ").replace(",", "."))
num_2 = float(input("Ingresa un numero: ").replace(",", "."))
num_3 = float(input("Ingresa un numero: ").replace(",", "."))
num_4 = float(input("Ingresa un numero: ").replace(",", "."))

## Treure decimals inecesaris (Decoratiu)
def rmvDecimals(num):
    if num == int(num):
        return int(num)
    return(num)
num_1 = rmvDecimals(num_1)
num_2 = rmvDecimals(num_2)
num_3 = rmvDecimals(num_3)
num_4 = rmvDecimals(num_4)

if num_1 > num_2:
    if num_3 > num_2:
        if num_1 > num_3:
            if num_4 > num_3:
                tiny = num_2
                small = num_3
                if num_4 > num_1:
                    medium = num_1
                    large = num_4
                else:
                    medium = num_4
                    large = num_1
            else:
                medium = num_3
                large = num_1
                if num_4 > num_2:
                    tiny = num_2
                    small = num_4
                else:
                    tiny = num_4
                    small = num_2
        else:
            if num_4 > num_1:
                tiny = num_2
                small = num_1
                if num_4 > num_3:
                    medium = num_3
                    large = num_4
                else:
                    medium = num_4
                    large = num_3
            else:
                medium = num_1
                large = num_3
                if num_4 > num_2:
                    tiny = num_2
                    small = num_4
                else:
                    tiny = num_4
                    small = num_2            
    else:
        if num_4 > num_2:
            tiny = num_3
            small = num_2
            if num_4 > num_1:
                medium = num_1
                large = num_4
            else:
                medium = num_4
                large = num_1
        else:
            medium = num_2
            large = num_1
            if num_4 > num_3:
                tiny = num_3
                small = num_4
            else:
                tiny = num_4
                small = num_3                  
else:
    if num_3 > num_1:
        if num_2 > num_3: 
            if num_4 > num_3:
                tiny = num_1
                small = num_3
                if num_4 > num_2:
                    medium = num_2
                    large = num_4
                else:
                    medium = num_4
                    large = num_2
            else:
                medium = num_3
                large = num_2
                if num_4 > num_1:
                    tiny = num_1
                    small = num_4
                else:
                    tiny = num_4
                    small = num_1      
        else:
            if num_4 > num_2:
                tiny = num_1
                small = num_2
                if num_4 > num_3:
                    medium = num_3
                    large = num_4
                else:
                    medium = num_4
                    large = num_3
            else:
                medium = num_2
                large = num_3
                if num_4 > num_1:
                    tiny = num_1
                    small = num_4
                else:
                    tiny = num_4
                    small = num_1              
    else:
        if num_4 > num_1:
            tiny = num_3
            small = num_1
            if num_4 > num_2:
                medium = num_2
                large = num_4
            else:
                medium = num_4
                large = num_2
        else:
            medium = num_1
            large = num_2
            if num_4 > num_3:
                tiny = num_3
                small = num_4
            else:
                tiny = num_4
                small = num_3  

print(str(tiny) + " " + str(small) + " " + str(medium) + " " + str(large))
    
