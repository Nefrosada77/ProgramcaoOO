class UnidadeMilitar:

    def __init__(self) -> None:
        print("Unidade Criada!")

    def Mover(self):
        print("Unidade Movimentando!")
    
    def Atacar(self):
        print("Unidade Atacando!")

class Soldado(UnidadeMilitar):

    def __init__(self) -> None:
        print("Soldado Criado")
    
    def mover(self):
        print("Soldado Movimentando por terra")

    def Atacar(self):
        print("Soldado Atacando")

class Arqueiro(UnidadeMilitar):

    def __init__(self) -> None:
        print("Arqueiro Criado")
    
    def mover(self):
        print("Arqueiro Movimentando por terra")

    def Atacar(self):
        print("Arqueiro Atacando a distancia")

class Cavaleiro(UnidadeMilitar):

    def __init__(self) -> None:
        print("Cavaleiro Criado")
    
    def mover(self):
        print("Cavaleiro Movimentando a cavalo")

    def Atacar(self):
        print("Soldado Atacando a cavalo")

Unidades = []

sol = Soldado()
arq = Arqueiro()
cava = Cavaleiro()

Unidades.append(sol)
Unidades.append(arq)
Unidades.append(cava)

for unity in Unidades:
    unity.mover()
    unity.Atacar()
