import random
class dado:
    def __init__(self,lados) -> None:
        self.lados = lados
    def rolar(self):
        nlados = []
        for a in range(1,self.lados+1):    
            nlados.append(a)
        print(nlados)
        for b in range(3):
            escolha = random.choice(nlados)
            return escolha
    
dadovirtual1 = dado(6)
print("O destino escolheu seu número:",dadovirtual1.rolar())
dadovirtual8 = dado(8)
print("O destino escolheu seu número:",dadovirtual8.rolar())
dadovirtual12 = dado(12)
print("O destino escolheu seu número:",dadovirtual12.rolar())