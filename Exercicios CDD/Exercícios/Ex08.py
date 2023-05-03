soma = 0

for x in range(10):
    num = int(input("Digite um número: "))
    if num%2 != 0:
        soma = soma + num

print(soma)