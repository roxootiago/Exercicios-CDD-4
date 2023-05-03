count = 0
countFora = 0
for x in range(5):
    num = int(input("Digite um número: "))

    if num >= 10 and num <= 20:
        count += 1

    else:
        countFora += 1

print(f"Dentro do intervalo: {count}")
print(f"Fora do intervalo: {countFora}")