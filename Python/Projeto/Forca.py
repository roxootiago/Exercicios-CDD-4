from champsGenerator import nameChampion,titleChamps


def Forca():
    def continuar():
        continuarGame = input("Você deseja continuar jogando? ").upper()
        if continuarGame == "S" or continuarGame == "SIM":
            Forca()
        else:
            print("Encerrando jogo...")

    def tentativa():
        tentar = input("\nVocê já sabe a resposta? ").upper()

        if tentar == "S" or tentar == "SIM":
            champTentativa = input("Digite sua tentativa: ").upper()
            if champTentativa == champsRand:
                print(f"Parabéns! Você acertou!\nCampeão selecionado: {champsRand}: {titleChamps().capitalize()}")
                continuar()
            else:
                print(champTentativa)
                print("Você errou! Tente novamente")
                Forca()
        else:
            continuar()

    champsRand = nameChampion().upper()
    emptyList = []
    count = 0

    print(" ---x--- JOGO DA FORCA ---x---")
    print("--- ADIVINHE O NOME DO CHAMP ---")

    for i in champsRand:
        count += 1
    #print(champsRand)
    print(f"\nDica: {titleChamps().capitalize()}\nO campeão tem {count} letras")
    for k in range(count):
        emptyList.append("_")

    for y in range(count):
        print(emptyList[y], end=" ")
    print()

    kick = input("Digite uma letra: ").upper()

    for z in range(count):
        if champsRand[z] == kick:
            emptyList[z] = kick

    for p in range(count):
        print(emptyList[p], end=" ")
    tentativa()


Forca()
