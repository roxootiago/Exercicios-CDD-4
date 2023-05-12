def somar(*num):
    total = 0
    for i in num:
        total += i
    return total

numeros = somar(2,3,4,7,6)
print(f"Total: {numeros}")
