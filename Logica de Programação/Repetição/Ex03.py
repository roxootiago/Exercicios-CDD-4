num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo número: "))

while num2 == 0:
    num2 = int(input("Digite o segundo número: "))

print(f"{num1} ÷ {num2} = {num1/num2:.2f}")