votosTotais = int(input("Qual o número total de eleitores? "))
votosBrancos = int(input("Qual o número de votos brancos? "))
votosNulos = int(input("Qual o número de votos nulos ?"))
votosValidos = int(input("Qual o número de votos válidos? "))
total = votosBrancos+votosNulos+votosValidos
percentualVotoBranco =total * votosBrancos / 100
percentualVotoNulo = total * votosNulos / 100
percentualVotoValido =total * votosValidos / 100

print(percentualVotoBranco)
print(percentualVotoNulo)
print(percentualVotoValido)
print(total)