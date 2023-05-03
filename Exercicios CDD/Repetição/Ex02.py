qntdAluno = int(input("Digite a quantidade de alunos: "))
count = 0

while count < qntdAluno:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    count += 1

media = (nota1 + nota2) / qntdAluno
print(f"{media:.2f}")
