# Escreva um algoritmo que receba do usuário 10 números, guarde num array e
# mostre:
# 1 - todos os números ímpares;
# 2 - todos os números pares;
# 3 - todos os números positivos;
# 4 - todos os números negativos;
# 5 - todos os zeros que aparecem no array;

A = []
impar = []
par = []
positivo = []
negativo = []
zero = []
for i in range(10):
    A.append(int(input("Digite um número: ")))

for j in range(10):
    if A[j] % 2 != 0:
        impar.append(A[j])
    else:
        par.append(A[j])
    if A[j] > 0:
        positivo.append(A[j])
    elif A[j] < 0:
        negativo.append(A[j])
    if A[j] == 0:
        zero.append(A[j])

for k in range(1):
    print(f"Ímpares: {impar}\nPares: {par}\nPositivos: {positivo}\nNegati"
          f"vos: {negativo}\nZero: {zero}")
