count = 0
countFora = 0
for x in range(3):
    num = int(input("Digite um número: "))

    if num in range(10,20+1):
     count += 1

    else:
        countFora += 1

print(f"Dentro do intervalo: {count}")
print(f"Fora do intervalo: {countFora}")