quantidadeAlunos = int(input("Digite a quantidade de alunos: "))
soma = 0

for x in range(quantidadeAlunos):
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    media = (nota1+nota2)/2
    print("-"*80)
    soma = soma +media

mediaTotal = soma/quantidadeAlunos

print(f"A média da turma é: {mediaTotal}")

