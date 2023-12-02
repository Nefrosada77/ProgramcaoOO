import random
class Animal:

    def __init__(self,nome) -> None:
        self.nome = nome
    
    def exibir_descricao(self):
        print(f"Nome do Animal: {self.nome}")

class Carnivoro(Animal):

    def __init__(self,nome) -> None:
        super().__init__(nome)

    def cacar(self):
        print(f"{self.nome} está caçando;")

    def exibir_descricao(self):
        super().exibir_descricao()
        print(f"{self.nome} é Carnivoro;")

class Herbivoro(Animal):

    def __init__(self,nome) -> None:
        super().__init__(nome)
    
    def pastar(self):
        print(f"{self.nome} está pastando;")

    def exibir_descricao(self):
        super().exibir_descricao()
        print(f"{self.nome} é Herbivoro")

class Onivoro(Carnivoro,Herbivoro):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def comer(self):
        escolha = random.randrange(0,1)
        if escolha == 0:
            super().cacar()
        elif escolha == 1:
            super().pastar()
        
    def exibir_descricao(self):
        print(f"{self.nome} é Onivoro;")
    
Inseto = Herbivoro("Formiga")
Mamifero = Onivoro("Ser Humano")
Outra_Coisa = Carnivoro("Leão")

Inseto.pastar()
Inseto.exibir_descricao()
Mamifero.comer()
Mamifero.exibir_descricao()
Outra_Coisa.cacar()
Outra_Coisa.exibir_descricao()
    
