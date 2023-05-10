from mercado import estoque
produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
valorUnid = float(input("Digite o valor unitário: R$"))


total = estoque(produto,quantidade,valorUnid)
print("-"*30)
print(f"Produto: {produto}\nQuantidade: {quantidade}\nValor unidade: R$"
      f"{valorUnid}\nValor total: R${total}")