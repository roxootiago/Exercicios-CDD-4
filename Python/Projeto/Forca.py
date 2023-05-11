from random import choice

def game():
    champs = ["KATARINA","AMUMU", "ZED"]
    lista = []

    print("---x--- JOGO DA FORCA ---x---")
    print("--- ADVINHE O NOME DO CHAMP ---")

    champsRand = choice(champs)

    # letras = len(champsRand)
    def tentativa():
        tentar = input("\nVocê já sabe a resposta? ").upper()

        if tentar == "S":
            champTentativa = input("Digite sua tentativa: ").upper()
            if champTentativa == champsRand:
                print(f"Parabéns! Você acertou!\nSeu chute: {champTentativa}")
            else:
                print("Você errou! Tente novamente")
                tentativa()
        else:
            print("Ok")

    count = 0
    for i in champsRand:
        count += 1

    print(f"O campeão tem {count} letras")
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

game()
