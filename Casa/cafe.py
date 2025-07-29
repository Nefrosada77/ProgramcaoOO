import random

class Container:

    def __init__(self,volume=int,capacidade=int) -> None:
        self.vol = volume
        self.cap = capacidade

class CopoCafe(Container):

    def __init__(self, volume=int, capacidade=int) -> None:
        super().__init__(volume, capacidade)
    
    def Beber(self):
        self.vol -= 1
    
    def Vazio(self):
        if self.vol >= 0:
            return True
    
    def Limpar(self):
        self.vol = 0

class CoofePot(Container):

    def __init__(self, volume=int, capacidade=int) -> None:
        super().__init__(volume, capacidade)
    
    def Vazio(self):
        if self.vol >= 0:
            return True
    
    def FazerCafe(self):
        self.vol = self.cap
    
    def Limpar(self):
        self.vol = 0
    
    def EncherCopo(self):
        praencher = copodecafe.cap - copodecafe.vol
        copodecafe.vol = copodecafe.cap
        self.vol -= praencher


copodecafe = CopoCafe(0,12)
maquina = CoofePot(0,32)