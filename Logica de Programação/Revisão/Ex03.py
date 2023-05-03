opcao = "S"
idades = []
while opcao == "S":

    idade = int(input("Digite sua idade: "))

    anoNascimento = (2023 - idade)
    idades.append(anoNascimento)
    print(f"Você nasceu em {anoNascimento}")

    opcao = input("Deseja calcular outra idade?\n(S) Sim\n(N) Não\nDigite sua opção: ").upper()

print(idades)