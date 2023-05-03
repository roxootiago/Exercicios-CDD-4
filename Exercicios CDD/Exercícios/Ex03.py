numCorrespondente = int(input("Digite um númerod e 1 a 12: "))

match numCorrespondente:
    case 1:
        print("O mês foi JANEIRO")

    case 2:
        print("O mês foi FEVEREIRO")

    case 3:
        print("O mês foi MARÇO")

    case 4:
        print("O mês foi ABRIL")

    case 5:
        print("O mês foi MAIO")

    case 6:
        print("O mês foi JUNHO")

    case 7:
        print("O mês foi JULHO")

    case 8:
        print("O mês foi AGOSTO")

    case 9:
        print("O mês foi SETEMBRO")

    case 10:
        print("O mês foi OUTUBRO")

    case 11:
        print("O mês foi NOVEMBRO")

    case 12:
        print("O mês foi DEZEMBRO")

    case _ :
        print("Valor inválido")