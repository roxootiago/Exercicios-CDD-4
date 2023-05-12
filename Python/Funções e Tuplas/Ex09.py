a = [1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8]
novalista = []


def funcao(a):
    for i in a:
        if i not in novalista:
            novalista.append(i)

    print(novalista)


funcao(a)
