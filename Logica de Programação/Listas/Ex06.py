tamanho = int(input("Digite o tamanho do vetor: "))
a = []
b=[]
c = []
for i in range(tamanho):
    a.append(float(input("Digite um número: ")))
    b.append(float(input("Digite outro número: ")))

for x in range(tamanho):
    c.append(a[x]+b[x])

print(c)