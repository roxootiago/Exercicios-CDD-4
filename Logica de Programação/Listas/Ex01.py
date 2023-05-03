qntdAluno = int(input("Quantos alunos tem na sala? "))
nomeAluno = []
for i in range (qntdAluno):
    nomeAluno.append (input("Digite o nome dos alunos: "))

for x in range (qntdAluno):
    print(f"{x}- {nomeAluno[x]}")
