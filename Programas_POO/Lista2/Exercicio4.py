import random
import os
from termcolor import colored
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
        if (self.pos % 5) == 0 and self.pos < 20:
            print(colored(f"{self.nome} derrapa na curva!!","red"))
            self.pos -= 1
        elif self.pos == 7 or self.pos == 17:
            print(colored(f"{self.nome} acelera com tudo!!","green"))
            self.pos += 2    
        elif self.pos == 13:
            print(colored(f"{self.nome} bateu o carro e terá que voltar para o inicio!!","white","on_red"))
            self.pos = 0
        if self.pos < 20:
            print("Posição de",self.nome,':',self.pos)
        if self.pos >= 20:
            print(colored(f"{self.nome} passa pela linha de chegada na posição: {self.pos}","yellow"))

    def getPos(self):
        return self.pos
    
dadovirtual1 = dado(6)
total = False
Competidores = []

os.system('cls' if os.name == 'nt' else 'clear')
print(colored("CORRIDA MALUCA","cyan", attrs=["bold","underline"]))
input("Entrar...")
os.system('cls' if os.name == 'nt' else 'clear')

while total != True:
    os.system('cls' if os.name == 'nt' else 'clear')
    Competidores.append(Competidor(input("Nome do competidor: ")))
    conc = input("Concluir? (S/N): ")
    if conc == "S" or conc == "s":
        total = True
    else:
        pass

vencedor = False
rodada = 1
while vencedor != True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Rodada:",rodada)
    for competidor in Competidores:
        competidor.atualizar(dadovirtual1.rolar())   
        pos = competidor.getPos()
        if pos >= 20:
            vencedor = True
    input("Continuar...")
    rodada += 1  