import self


class Atleta:
    def __init__(self, peso):
        self.peso = peso
        self.aposentado = False
        self.aquecido = True

    def aposentar(self):
        if not self.aposentado:
            self.aposentado = True
            print("O atleta está aposentado")

    def aquecer(self):
        if not self.aposentado:
            if not self.aquecido:
                print("O atleta foi aquecer")
                self.aquecido = True
            else:
                print("O atleta já está aquecido")


class corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def correr(self):
        if not self.aposentado and self.aquecido:
            print("O atleta pode correr")
        else:
            print("O atleta não pode correr")


class nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def correr(self):
        if not self.aposentado and self.aquecido:
            print("O atleta pode nadar")
        else:
            print("O atleta não pode nadar")


class ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def correr(self):
        if not self.aposentado and self.aquecido:
            print("O atleta pode pedalar")
        else:
            print("O atleta não pode pedalar")


class triatleta(ciclista, nadador, corredor):
    def __init__(self, peso):
        super().__init__(peso)

    def exercicio(self):
        if not self.aposentado and self.aquecido:
            print("o atleta correr")


jao = Atleta(55)
jao.aposentar()
jao.aquecer()
tiago = corredor(50)
tiago.correr()
carlo = triatleta(80)
carlo.correr()
