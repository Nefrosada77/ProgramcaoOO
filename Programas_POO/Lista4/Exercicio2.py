class Veiculo:

    def __init__(self,marca,modelo,ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano        

    def acelerar(self):
        print("Acelerando o veículo!")
    
    def frear(self):
        print("Freando o veículo!")
    

class Carro(Veiculo):

    def __init__(self, marca, modelo, ano, cor) -> None:
        super().__init__(marca, modelo, ano)
        self.cor = cor
    
    def ligar_radio(self):
        print("Ligando o rádio do carro!")
    
    def abrir_porta(self):
        print("Abrindo a porta do carro!")

class Moto(Veiculo):

    def __init__(self, marca, modelo, ano, cilindrada) -> None:
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def empinar(self):
        print("Empinando a moto!")
    
    def buzinar(self):
        print("Buzinando a moto!")

class Caminhao(Veiculo):

    def __init__(self, marca, modelo, ano, carga_maxima) -> None:
        super().__init__(marca, modelo, ano)
        self.carga = carga_maxima
    
    def carregar(self):
        print("Carregando o caminhão!")
    
    def descarregar(self):
        print("Descarregando o caminhão!")
    
carro = Carro("Chevrolet","Prisma","2023","Preto")
carro.abrir_porta()
carro.ligar_radio()
carro.acelerar()
carro.frear()

moto = Moto("Honda","X-ADV","2023","745")
moto.buzinar()
moto.acelerar()
moto.frear()
moto.empinar()

caminhao = Caminhao("Volkswagem","Constellation","2020","18t")
caminhao.carregar()
caminhao.acelerar()
caminhao.frear()
caminhao.descarregar()