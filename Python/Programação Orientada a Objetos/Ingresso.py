class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def ImprimeValor(self):
        print(f"O valor do ingresso é R${self.valor}")


class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def ImprimeValor(self, percentual):
        print(f"O valor do ingresso VIP custa: {(self.valor * percentual / 100) + self.valor:.2f}")


valorIngresso1 = int(input("Digite o valor do ingresso: R$"))

valorIngresso = Ingresso(valorIngresso1)
valorIngresso.ImprimeValor()

ingressoVip = IngressoVip(valorIngresso1)
ingressoVip.ImprimeValor(50)
