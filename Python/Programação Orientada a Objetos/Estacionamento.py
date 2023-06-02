from random import choice


class Estacionamento:
    def __init__(self, quantidadeVagas):
        self.vagas = None
        self.vagaSelecionada = None
        self.quantidadeVagas = quantidadeVagas
        self.vagasLivres = 0
        self.vagasoOcupadas = 1
        self.count = 0

    def vagasEstacionamento(self):
        self.vagas = []
        for i in range(1, self.quantidadeVagas + 1):
            self.vagas.append(i)

    def Estacionar(self):
        self.vagaSelecionada = choice(self.vagas)
        for j in range(len(self.vagas)):
            if self.vagaSelecionada in self.vagas:
                self.vagas.pop(self.vagas[j])
        self.count += 1

    def exibirTeste(self):
        print(self.vagas)


carro = Estacionamento(5)
carro.vagasEstacionamento()
carro.exibirTeste()
carro.Estacionar()
carro.exibirTeste()
carro.Estacionar()
carro.exibirTeste()
