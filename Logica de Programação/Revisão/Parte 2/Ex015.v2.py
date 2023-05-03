
# Escreva um algoritmo para ler a hora de
# início e a hora de fim de um jogo de Xadrez (
# considere apenas horas inteiras sem os
# minutos) e calcule a duração do jogo em
# horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo
# pode inicar em um dia e terminar no dia seguinte

horaInicio = int(input("Digite a hora de início da partida: "))
horaFinal = int(input("Digite a hora final: "))

if horaInicio < horaFinal:
    print(f"O jogo durou {horaInicio - horaFinal}h")
else:
    print(f"O jogo durou mais de {24 - (horaInicio - horaFinal)}!")