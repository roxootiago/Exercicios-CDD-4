votosTotais = int(input("Qual o número total de eleitores? "))
votosBrancos = int(input("Qual o número de votos brancos? "))
votosNulos = int(input("Qual o número de votos nulos ?"))
votosValidos = int(input("Qual o número de votos válidos? "))

percentualVotoBranco =votosTotais * votosBrancos / 100
percentualVotoNulo = votosTotais * votosNulos / 100
percentualVotoValido =votosTotais * votosValidos / 100

print(percentualVotoBranco)
print(percentualVotoNulo)
print(percentualVotoValido)
print(votosTotais)