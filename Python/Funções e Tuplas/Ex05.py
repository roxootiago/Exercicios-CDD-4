def estoque(nome, qtd, valorUnit):
    return nome, qtd * valorUnit


produto = input("Digite o produto: ")
quantidade = int(input("Digite a quantidade: "))
valor = float(input("Digite o valor: R$"))
prod,total = estoque(produto, quantidade, valor)

print("-" * 30)
#print(f"Produto: {total[0]}\nDeu: R${total[1]}")
print(f"Produto {prod}\nValor total: R${total}")
