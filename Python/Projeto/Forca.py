from random import choice
champs = ["YASUO","KATARINA","JINX","WUKONG","ZED"]

print("---x--- JOGO DA FORCA ---x---")
print("--- ADVINHE O NOME DO CHAMP ---")


champsRand = choice(champs)
#letras = len(champsRand)

count = 0
for i in champsRand:
    count += 1

print(f"O campeão tem {count} letras")
print(f" _ "*count)

letra = input("Digite uma letra: ")