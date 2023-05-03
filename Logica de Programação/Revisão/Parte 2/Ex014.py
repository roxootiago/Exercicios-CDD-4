# Escreva um algoritmo para ler dois valores (
# considere que não serão lidos valores iguais)
# e escrevê-los em ordem crescente

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(num2,num1)
else:
    print(num1,num2)