while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(
        "Escolha uma das opções:\n(1) Soma\n(2) Subtração\n(3) Multiplicação\n(4) Divisão\n(5) Para digitar novo número\n(6) Para Sair")
    escolha = int(input("Digite sua opcao: "))

    match escolha:
        case  1:
            print(f"{num1} + {num2} = {num1+num2}")

        case  2:
            print(f"{num1} - {num2} = {num1-num2}")

        case  3:
            print(f"{num1} x{num2} = {num1*num2}")

        case  4:
            print(f"{num1} ÷ {num2} = {num1/num2}")

        case  5:
            continue

        case 6:
            break

print("Fim do programa!")