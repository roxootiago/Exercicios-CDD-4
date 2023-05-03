#Usando While escreva um algoritmo que preencha um array A com os 10
# primeiros números ímpares, iniciando por zero

#saída: [1,3,5,7,9,11,13,15,17,19]

A = []
count = 0
countImpar = 0
while countImpar <= 10:
    if count %2 != 0:
        A.append(count)
        countImpar +=1
    count+=1
print(A)