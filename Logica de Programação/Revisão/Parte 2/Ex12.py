# Escreva um algoritmo para ler o número total
# de eleitores de um município, o número de
# votos brancos, nulos e válidos. Calcular e
# escrever o percentual que cada um representa
# em relação ao totl de eleitores:

votosTotais = int(input("Qual o número total de eleitores? "))
votosBrancos = int(input("Qual o número de votos brancos? "))
votosNulos = int(input("Qual o número de votos nulos ?"))
votosValidos = int(input("Qual o número de votos válidos? "))

totalVotos = votosBrancos + votosNulos + votosValidos

percentualVotoBranco = votosTotais * votosBrancos/ 100
percentualVotoNulo = votosTotais * votosNulos / 100
percentualVotoValido =votosTotais * votosValidos / 100
if totalVotos == votosTotais:
    print(f"{percentualVotoBranco}%")
    print(f"{percentualVotoNulo}%")
    print(f"{percentualVotoValido}%")
    print(f"{votosTotais}%")

