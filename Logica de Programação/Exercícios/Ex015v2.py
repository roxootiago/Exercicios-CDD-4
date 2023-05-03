opcao = "S"

while opcao == "S":
    nota1 = float(input("Digite a primeira nota: "))

    while nota1 < 0 or nota1 > 10:
        print("Digite uma nota válida!")
        nota1 = float(input())

    nota2 = float(input("Digite a segunda nota: "))

    while nota2 < 0 or nota2 > 10:
        print("Digite uma nota válida!")
        nota2 = float(input())

    print(f"Av1: {nota1}\nAv2: {nota2}\nMédia:{(nota1 + nota2) / 2}")

    opcao = input("Deseja continuar?\n(S) Sim\n(N) Não\n").upper()



