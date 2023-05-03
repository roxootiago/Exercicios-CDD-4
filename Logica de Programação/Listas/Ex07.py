num = []
count = 0
for i in range(3):
    num.append (float(input("Digite um número: ")))

num2 = int(input("Digite outro número: "))

for x in range(3):
    if num2 == num[x]:
        count += 1

print(count)