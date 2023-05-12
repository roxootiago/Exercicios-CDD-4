def numeros(a):
    if a % 2 != 0:
        return("N!")
    elif a == 0:
        return("Z!")
    else:
        return("P!")

print(numeros(4))
print(numeros(-3))
print(numeros(0))