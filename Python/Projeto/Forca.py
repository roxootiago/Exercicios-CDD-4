from champsGenerator import champs


def game2():
    def continuar():
        continuarGame = input("Você deseja continuar jogando? ").upper()
        if continuarGame == "S" or continuarGame == "SIM":
            game2()
        else:
            print("Encerrando jogo...")

    def tentativa():
        tentar = input("\nVocê já sabe a resposta? ").upper()

        if tentar == "S" or tentar == "SIM":
            champTentativa = input("Digite sua tentativa: ").upper()
            if champTentativa == champsRand:
                print(f"Parabéns! Você acertou!\nSeu chute: {champTentativa}")
                continuar()
            else:
                print("Você errou! Tente novamente")
                game2()
        else:
            continuar()

    champsRand = champs()
    lista = []
    count = 0

    for i in champsRand:
        count+=1
    print(champsRand)
    print(f"\nO campeão tem {len(champsRand)} letras")
    for k in range(count):
        lista.append("_")

    for y in range(count):
        print(lista[y], end=" ")
    print()

    letra = input("Digite uma letra: ").upper()

    for z in range(count):
        if champsRand[z] == letra:
            lista[z] = letra

    for p in range(count):
        print(lista[p], end=" ")
    tentativa()


print(" ---x--- JOGO DA FORCA ---x---")
print("--- ADIVINHE O NOME DO CHAMP ---")

game2()
