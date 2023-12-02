class Assinatura:

    def __init__(self) -> None:
        pass

    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    
    def __init__(self) -> None:
        pass

    def calcular_preco(self):
        print("Assinatura Simples:\nPreço: R$29,99;\n")
    
    def exibir_detalhes(self):
        print("Assinatura Simples:\nAcesso a Filmes e Series em Qualidade Padrão;\n")

class AssinaturaPremium(Assinatura):
    
    def __init__(self) -> None:
        pass

    def calcular_preco(self):
        print("Assinatura Premium:\nPreço: R$49,99;\n")

    def exibir_detalhes(self):
        print("Assinatura Premium:\nAcesso a Filmes e Séries em Qualidade HD e Ultra HD\n")
    
simples = AssinaturaSimples()
premium = AssinaturaPremium()
assinaturas = []
assinaturas.append(simples)
assinaturas.append(premium)
for assinatura in assinaturas:
    assinatura.calcular_preco()
    assinatura.exibir_detalhes()