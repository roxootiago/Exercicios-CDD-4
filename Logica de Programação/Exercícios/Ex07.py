num = int(input("Digite um número: "))
impar = []
par = []
for i in range(1,num+1):
    if i%2 != 0:
        impar.append(i)
    else:
        par.append(i)


print(f"Números ímpares: {impar}")
print(f"Números pares: {par}")
