import math
class FormaGeormetrica:
    def __init__(self) -> None:
        pass

class Retangulo(FormaGeormetrica):
    def __init__(self,altura = float,base = float) -> None:
        super().__init__()
        self.altura = altura
        self.base = base
    
    def CalcularArea(self):
        area = float(self.altura * self.base)
        print("Area do Retangulo: ",area)
    
    def CalcularPerimetro(self):
        perimetro = float((self.altura * 2) + (self.base * 2))
        print("Perimetro do Retangulo: ",perimetro)

class Triangulo(FormaGeormetrica):
    def __init__(self,altura = float,base = float) -> None:
        super().__init__()
        self.altura = altura
        self.base = base
    
    def CalcularArea(self):
        area = float((self.altura * self.base)/2)
        print("Area do Triangulo Retangulo: ",area)
    
    def CalcualrPerimetro(self):
        perimetro = float(self.base + self. altura + (((self.base ** 2 + self.altura ** 2)** 0.5)))
        print("Perimetro do Triangulo Retangulo: ",perimetro)

class Circulo(FormaGeormetrica):
    def __init__(self,raio = float) -> None:
        super().__init__()
        self.raio = raio

    def CalcularArea(self):
        area = float(math.pi*(self.raio ** 2))
        print("Area do Circulo: ",area)
    
    def CalcularCircunferencia(self):
        circunferencia = float(2*math.pi*self.raio)
        print("Circunferencia: ",circunferencia)


Reta = Retangulo(5,5)
Reta.CalcularArea()
Reta.CalcularPerimetro()

Tri = Triangulo(3,4)
Tri.CalcularArea()
Tri.CalcualrPerimetro()

Circo = Circulo(2)
Circo.CalcularArea()
Circo.CalcularCircunferencia()
