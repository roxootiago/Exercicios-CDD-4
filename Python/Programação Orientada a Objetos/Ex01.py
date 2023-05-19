class Pessoa:
    def __init__(self, nome, idade,
                 peso, comendo=False, falar=
                 False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = comendo
        self.falar = falar

    def __str__(self):
        return f"Nome: {self.nome}\nIdade:" \
               f"{self.idade}"

    def Comer(self, ali):
        self.ali = ali

        self.falar = True
        if self.falar == True and \
                self.comendo == False:
            print(f"Você não pode comer pois "
                  f"está falando")
            self.falar = False
            self.comendo = True
        elif self.falar == False and \
                self.comendo == True:
            print(f"{self.nome} está comendo "
                  f"{ali}")
            self.comendo = True
        elif self.comendo == True:
            print(f"{self.nome} já está "
                  f"comendo")


    def PararDeComer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} não estava "
                  f"comendo")

    def Falar(self, falar=False):
        self.falar = falar
        if self.comendo == True:
            print(f"Não pode falar pois está "
                  f"comendo")
        else:
            print(f"Agora pode falar")
            self.falar = True

    def PararDeFalar(self):
        if self.falar == True:
            print(f"{self.nome} parou de falar")
            self.falar = False
        else:
            print(f"{self.nome} continua falando")
