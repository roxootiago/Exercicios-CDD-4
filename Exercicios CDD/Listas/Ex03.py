a = []
m = []
soma = 0
for x in range(4):
    num1 = float(input("Digite um número: "))
    a.append(num1)

num3 = a.pop()
print(f"Número multiplicador: {num3}")

for x in a:
    m.append(x*num3)

for x in m:
    print(x)
