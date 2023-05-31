import datetime


class Conta:
    def __init__(self, numero, titular, conta):
        self.__numero = numero
        self.titular = titular
        self.__conta = conta
        self.saldo = 0
        self.__limite = 0
        self.__taxaDeTransferencia = 5.90
        self.__codigoBanco = "020"
        self.ativa = False

    def AtivarConta(self):
        self.ativa = True
        print(f"A conta do titular "
              f"{self.titular} está ativa")

    def DesativarConta(self):

        if self.saldo > 0:
            print("A conta não pode ser "
                  "desativada pois ainda "
                  "tem saldo")
        elif self.ativa and self.saldo <= 0:
            print("A conta está desativada")

    def Extrato(self):
        if not self.ativa:
            print("Ative a conta para ver o "
                  "extrato")
        else:
            print(
                f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
                f"Titular: {self.titular}\nConta: {self.__conta}\nSaldo: R$"
                f"{self.saldo}\nData do extrato:"
                f" {datetime.datetime.now().strftime('%d')}/"
                f"{datetime.datetime.now().strftime('%m')}/"
                f"{datetime.datetime.now().strftime('%Y')}\nHora "
                f"do "
                f"extrato: "
                f"{datetime.datetime.now().strftime('%I')}:"
                f"{datetime.datetime.now().strftime('%M')}"
                f"{datetime.datetime.now().strftime('%p').lower()}\n")

    def Depositar(self, valor):
        if not self.ativa:
            print("Ative a conta para depositar")
        else:
            self.saldo += valor

    def __ValorDisponivel(self, valor):
        valorDisponivel = self.saldo + self.__limite
        return valor <= valorDisponivel

    def Sacar(self, valor):
        if not self.ativa:
            print("Ative a conta para sacar")
        else:
            if self.__ValorDisponivel(valor):
                self.saldo -= valor
                print(
                    f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\nSeu saque foi "
                    f"concluído!\nValor sacado: R${valor}\nValor atual: R${self.saldo}")
            else:
                print(
                    "Saldo insuficiente para saque!")

    def __PodeTransferir(self, valor):
        ValorDisponivelTransferencia = (
                                               self.saldo + self.__limite) - self.__taxaDeTransferencia
        return valor <= ValorDisponivelTransferencia

    def Transferir(self, valor, destino):
        if not self.ativa:
            print("Ative a conta para transferir")
        else:
            if self.__PodeTransferir(valor):
                self.Sacar(valor)
                destino.Depositar(valor)
                print(
                    f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
                    f"Você recebeu uma transferência de {self.titular.upper()}"
                    f"\nValor"
                    f" recebido: R${valor:.2f}\nData da transferência:"
                    f" {datetime.datetime.now().strftime('%d')}/"
                    f"{datetime.datetime.now().strftime('%m')}/"
                    f"{datetime.datetime.now().strftime('%Y')}\nHora "
                    f"da transferência: "
                    f"{datetime.datetime.now().strftime('%I')}:"
                    f"{datetime.datetime.now().strftime('%M')}"
                    f"{datetime.datetime.now().strftime('%p').lower()}\n")
            else:
                print(
                    "Saldo insuficiente para transferência!")

    def __set_limite(self, newLimite):
        self.__limite += newLimite
        return self.__limite

    def AumentoDeLimite(self, valor):
        if not self.ativa:
            print("Ative a conta primeiro!")
        else:
            print(
                f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
                f"Olá, {self.titular}\nSeu limite do cartão foi de R$"
                f"{self.__limite} para R${self.__set_limite(valor)}")

    @staticmethod
    def CodigoBanco():
        return "001"


outraRef = None  # aponta para nenhuma referência
