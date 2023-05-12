a = [1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8]
novalista = []


def funcao():
    for i in a:
        if a[i] != novalista[i]:
            novalista.append(i)

    print(novalista)


funcao()
