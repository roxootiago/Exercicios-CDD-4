a = [1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8]
novalista = []

def funcao(a):
    for i in range(len(a)):
        if a[i] not in novalista:
            novalista.append(a[i])

    print(novalista)

funcao(a)
