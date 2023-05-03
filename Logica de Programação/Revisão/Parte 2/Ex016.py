# As maçãs custam R$1,30 cada se forem
# compradas menos de uma dúzia, e R$1,00 se
# forem compradas pelo menos 12, Escreva um
# programa que leia o número de maçãs
# compradas, calule e escreva o custo total da
# compra

quantidadeMaca = int(input("Quantas maçãs foram compradas? "))

if quantidadeMaca < 12:
    print(f"{quantidadeMaca} custa: R${quantidadeMaca*1.30:.2f}")

else:
    print(f"{quantidadeMaca}: R$ {quantidadeMaca} ")

