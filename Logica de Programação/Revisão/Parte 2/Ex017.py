#Escreva um algoritmo que dado um array, retorne um novo array, com os
# elementos em oredm invertida
#entrada : a = [2,5,4,2,8,5,2]
#saída: b = [2,5,8,2,4,5,2]

A = [2,5,4,2,8,5,2]
B= []

for j in range(-1,-8,-1):
    B.append(A[j])

print(A)
print(B)
