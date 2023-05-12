def somar(*num):
    return num

i = somar(3,2,4,1)

print(i)

soma = 0

for j in range(len(i)):
    soma = soma + i[j]

print(soma)