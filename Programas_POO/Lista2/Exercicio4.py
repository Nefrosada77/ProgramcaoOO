import random
import os
class dado:
    def __init__(self,lados) -> None:
        self.lados = lados
    def rolar(self):
        nlados = []
        for a in range(1,self.lados+1):    
            nlados.append(a)
        for b in range(3):
            escolha = random.choice(nlados)
            return escolha
    
class Competidor:
    def __init__(self,nome) -> None:
        self.nome = nome 
        self.pos = 0
    
    def atualizar(self,dado):
        self.pos += dado
        if (self.pos % 5) == 0:
            print(self.nome,"Derrapa na curva!!")
            self.pos -= 1
        elif self.pos == 7 or self.pos == 17:
            print(self.nome,"Acelera com tudo!!")
            self.pos += 2    
        elif self.pos == 13:
            print(self.nome,"Bateu o carro e terá que voltar para o inicio!!")
            self.pos = 0

            
    def getPos(self):
        return self.pos
    
dadovirtual1 = dado(6)
competidor1 = Competidor("Gabriel")
competidor2 = Competidor("Heitor")
competidor3 = Competidor("Rafael")
competidor4 = Competidor("Lucas")
competidor5 = Competidor("Matheus")
competidor6 = Competidor("Guilherme")
vencedor = False
rodada = 1
while vencedor != True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Rodada:",rodada)
    competidor1.atualizar(dadovirtual1.rolar())
    competidor2.atualizar(dadovirtual1.rolar())
    competidor3.atualizar(dadovirtual1.rolar())
    competidor4.atualizar(dadovirtual1.rolar())
    competidor5.atualizar(dadovirtual1.rolar())
    competidor6.atualizar(dadovirtual1.rolar())
    posicaocomp1 = competidor1.getPos()
    posicaocomp2 = competidor2.getPos()
    posicaocomp3 = competidor3.getPos()
    posicaocomp4 = competidor4.getPos()
    posicaocomp5 = competidor5.getPos()
    posicaocomp6 = competidor6.getPos()
    if posicaocomp1 >= 20:
        print("Gabriel passa pela linha de chegada na posição:",posicaocomp1)
        vencedor = True
    if posicaocomp1 < 20:
        print("Posição de Gabriel:",posicaocomp1)
    if posicaocomp2 >= 20:
        print("Heitor passa pela linha de chegada na posição:",posicaocomp2)
        vencedor = True
    if posicaocomp2 < 20:
        print("Posição de Heitor:",posicaocomp2)
    if posicaocomp3 >= 20:
        print("Rafael passa pela linha de chegada na posição:",posicaocomp3)
        vencedor = True
    if posicaocomp3 < 20:
        print("Posição de Rafael:",posicaocomp3)
    if posicaocomp4 >= 20:
        print("Lucas passa pela linha de chegada na posição:", posicaocomp4)
        vencedor = True
    if posicaocomp4 < 20:
        print("Posição de Lucas:",posicaocomp4)
    if posicaocomp5 >= 20:
        print("Matheus passa pela linha de chegada na posição:", posicaocomp5)
        vencedor = True
    if posicaocomp5 < 20:
        print("Posição de Matheus:",posicaocomp5)
    if posicaocomp6 >= 20:
        print("Guilherme passa pela linha de chegada na posição:", posicaocomp6)  
        vencedor = True
    if posicaocomp6 < 20:
        print("Posição de Guilherme:",posicaocomp6)
    input("Continuar...")
    rodada += 1  