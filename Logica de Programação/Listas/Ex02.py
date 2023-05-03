notas = []
alunosAprovados = []
soma = 0
cont = 0

qntdAluno = int(input("Quantos alunos tem na sala: "))

for i in range (qntdAluno):
    nomeAluno = (input("Digite o nome do aluno: "))
    notas.append(float(input("Digite a nota do aluno: ")))


for j in range (qntdAluno):
    soma += notas[j]

media = soma/qntdAluno

for x in range(qntdAluno):
    if media > notas[x]:
        cont += 1
        alunosAprovados.append(nomeAluno)

print(f"A quantidade de alunos acima da média é: {cont}")

for b in alunosAprovados:
    print(f"Alunos aprovados foram: {b}")