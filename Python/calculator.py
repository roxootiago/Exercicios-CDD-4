from operacoes import somar,subtrair,multiplicar,dividir

opcao = 0

while opcao != 5:


    opcao = int(input("Escolha uma opção:\n1 - Somar\n2-Subtração\n3- "
                    "Multiplicação\n4-Divisão\n5 - Sair\nDigite sua opção: "))
    match opcao:
        case 1:
            n1 = float(input("Digite o n2: "))
            n2 = float(input("Digite o n1: "))
            somar(n1,n2)
            break
        case 2:
            n1 = float(input("Digite o n2: "))
            n2 = float(input("Digite o n1: "))
            subtrair(n1,n2)
        case 3:
            n1 = float(input("Digite o n2: "))
            n2 = float(input("Digite o n1: "))
            multiplicar(n1,n2)
        case 4:
            n1 = float(input("Digite o n2: "))
            n2 = float(input("Digite o n1: "))
            dividir(n1,n2)
        case 5:
            break