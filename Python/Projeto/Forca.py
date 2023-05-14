from champsGenerator import nameChampion, titleChamps


def Forca():
    def continuar():
        continuarGame = input("Você deseja continuar jogando? ").upper()
        if continuarGame == "S" or continuarGame == "SIM":
            Forca()
        else:
            print("Encerrando jogo...")

    def tentativa():
        champTentativa = input("Digite sua tentativa: ").upper()
        if champTentativa == champsRand:
            print(
                f"Parabéns! Você acertou!\nCampeão selecionado: {champsRand}: {titleChamps().capitalize()}")
            opcao = input("Deseja jogar novamente").upper()
        else:
            print(champTentativa)
            print("Você errou! Tente novamente")
            jogar()
            tentativa()

    print(" ---x--- JOGO DA FORCA ---x---")
    print("--- ADIVINHE O NOME DO CHAMP ---")

    champsRand = nameChampion().upper()
    emptyList = []

    print(champsRand)
    print(f"\nDica: {titleChamps().capitalize()}\nO campeão tem {len(champsRand)} letras")

    def jogar():

        for k in range(len(champsRand)):
            emptyList.append("_")

        for t in range(len(champsRand)):
            if "'" in champsRand[t]:
                emptyList[t] = "'"
            if " " in champsRand[t]:
                emptyList[t] = " "

        for y in range(len(champsRand)):
            print(emptyList[y], end=" ")
        print()

        kick = input("Digite uma letra ou 'tentar' para tentar a palavra: ").upper()

        if kick == "TENTAR":
            tentativa()
        elif kick != "TENTAR":
            for z in range(len(champsRand)):
                if champsRand[z] == kick:
                    emptyList[z] = kick
                elif kick not in champsRand:
                    print("esta letra não está presente")
                    break
            for p in range(len(champsRand)):
                print(emptyList[p], end=" ")
            jogar()

    return jogar()


Forca()
