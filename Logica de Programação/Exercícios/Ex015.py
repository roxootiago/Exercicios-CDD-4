
##nota2 = float(input("Digite a segunda nota:"))

while True:
    nota1 = float(input("Digite uma nota: "))
    if nota1 >= 0 and nota1 <= 10:
        break
    else:
        print("Digite uma nota válida!")

while True:
    nota2 = float(input("Digite a segunda nota: "))
    if nota2 >= 0 and nota2 <= 10:
        break
    else:
        print("Digite uma nota válida!")

print(f"A média do aluno foi: {(nota1 + nota2)/2}")
