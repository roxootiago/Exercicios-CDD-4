contador = 0
soma = 0
while contador < 3:
    num = float(input("Digite um valor: "))

    soma += num
    contador += 1

print(f"a média de {soma} é: {soma/3:.2f}")