num = []
maiorValor = 0
menorValor = 0
count = 0
soma = 0
for i in range(3):
    num.append (int(input("Digite um número: ")))
    soma += num[i]

for j in range(3):
    if num[j] % 2 == 0:
        print(num[j],end=" ")

for x in range(3):
    maior = num[0]
    if num[x] > maior:
        maior = num[x]

for p in range(3):
    menor = num[0]
    if num[x] < menor:
        menor = num[x]


    media = soma / 3
for y in range(3):
    if num[y] > media:
        count += 1

print(f"\n{media:.2f}")
print(f"\no maior valor é: {maiorValor} e o menor valor é:  {menorValor}")
print(f"Existem {count} acima da média")