#Dado o seguinte array A = [10,12,20,30,25,40,32,32,35,50,60]. Crie um novo
# array com dados que estão entre índices 3 e 8.
A = [10,12,20,30,25,40,32,32,35,50,60]
B = []

for i in range (3,9):
        B.append(A[i])

print(B)