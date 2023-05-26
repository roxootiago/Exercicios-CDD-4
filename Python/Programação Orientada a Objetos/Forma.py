class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def CalcularArea(self, altura, base):
        print(f"{altura * base}")

    def CalcularPerimetro(self,altura, base):
        print(f"{altura * 2 + base * 2}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def CalcularArea(self,altura,base):
        print(f"{(base*altura)/2}")


ret = Retangulo()
ret.CalcularArea(2, 3)
ret.CalcularPerimetro(2,3)
