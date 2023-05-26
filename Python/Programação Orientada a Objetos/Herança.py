class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} comeu")

    def EmitirSom(self):
        print("emitiu som")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def EmitirSom(self):
        print(f"miaw miaw miaw")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def EmitirSom(self):
        print("ruf ruf ruf")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


chaninho = Gato("gnar", "laranja")
chaninho.EmitirSom()

dogMal = Cachorro("Nasus", "Preto")
dogMal.EmitirSom()

alistouro = Vaca("alistar", "roxo")

alistouro.EmitirSom()

