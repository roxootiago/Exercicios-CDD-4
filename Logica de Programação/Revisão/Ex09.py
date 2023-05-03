anos = int(input("Digite quantos anos você tem? "))
meses = int(input("Digite quantos meses: "))
dias = int(input("Digite quantos dias: "))

mesesAniversario = meses*30
anosAniversario = anos*365

print(f"Sua idade em dias é {mesesAniversario+anosAniversario+dias}")