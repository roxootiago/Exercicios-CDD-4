
texto = input("Digite um texto: ").lower()
def contar (a):
    vogais = ['a','e','i','o','u']
    count = 0

    for i in a:
        if i in vogais:
            count+=1

    print(count)

contar(texto)
print(texto)

