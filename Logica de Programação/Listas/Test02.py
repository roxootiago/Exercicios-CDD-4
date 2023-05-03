linguagens = ["Python","Javascript","Java"]
linguagens2 = ["TypeScript","React","Vue"]

print(linguagens)
print(linguagens+linguagens2)#Concatena listas
print(linguagens*2)#Repete listas
print("Java" in linguagens)#Verifica se existe na lista

for i,valor in enumerate (linguagens):#lista com indice
    print(f"{i}. {valor}")

linguagens.append("Ruby")#adicionando na última posição
print(linguagens)

linguagens.insert(2,"Django")
print(linguagens)



