numCorrespondente = int(input("Digite um númerod e 1 a 12: "))

if numCorrespondente > 12 or numCorrespondente < 1:
    print("Mês invalido")

else:
    if numCorrespondente == 1:
        print("O mês digitado foi JANEIRO")
    elif numCorrespondente ==  2:
        print("O mês digitado foi FEVEREIRO")
    elif numCorrespondente ==  3:
        print("O mês digitado foi MARÇO")
    elif numCorrespondente ==  4:
        print("O mês digitado foi ABRIL")
    elif numCorrespondente ==  5:
        print("O mês digitado foi MAIO")
    elif numCorrespondente ==  6:
        print("O mês digitado foi JUNHO")
    elif numCorrespondente ==  7:
        print("O mês digitado foi JULHO")
    elif numCorrespondente ==  8:
        print("O mês digitado foi AGOSTO")
    elif numCorrespondente ==  9:
        print("O mês digitado foi SETEMBRO")
    elif numCorrespondente ==  10:
        print("O mês digitado foi OUTUBRO")
    elif numCorrespondente ==  11:
        print("O mês digitado foi NOVEMBRO")
    else:
        print("O mês digitado foi DEZEMBRO")