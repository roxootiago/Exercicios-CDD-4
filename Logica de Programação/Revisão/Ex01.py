opcao = "S"
aprovado=[]
recuperacao = []
reprovado = []
media2 = []
count = 0
count1 = 0
count2 = 0

while opcao == "S":
    nota1  = float(input("Digite a primeira nota: "))
    nota2  = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    media2.append(media)

    if media >= 7 and media <= 10:
        print(f"O aluno foi aprovado com a média: {media}")
        aprovado.append(media)
        count += 1

    elif  media >= 4:
        print(f"O aluno foi para a recuperação com a média: {media}")
        recuperacao.append(media)
        count1 += 1

    elif  media >= 0:
        print(f"O aluno foi reprovado com a média: {media}")
        reprovado.append(media)
        count2 +=1
    else:
        print("Digite uma nota válida")

    opcao = input("Deseja fazer uma nova operação: \n(S) Sim\n(N) Não\nDigite uma opção: ").upper()

for i in range(len(media2)):
        print(f"| {media2[i]}",end = " ")

print(f"\nAlunos aprovados: {count}\nAlunos em recuperação: {count1}\nAlunos reprovados: {count2}")


