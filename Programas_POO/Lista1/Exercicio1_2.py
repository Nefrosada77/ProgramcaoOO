# Definição da classe Mago 

class Mago:
    # Atributos de classe
    possuiMagia = True

    # Método construtor
    def __init__(self, nome, idade, escola, poder, elemento):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.poder = poder 
        self.elemento = elemento
        print('Mago ', self.nome, ' foi criado!')

    # Outros métodos    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def verificar_poder(self):
        print('Meu poder é: ',self.poder)

    def verificar_elemento(self):
        print('Meu Elemento é: ',self.elemento)

    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 
    
        
        
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts', 10, 'magia')
gd = Mago('Gandalf', 2000, 'Magia Cinza', 500, 'elemental')
mm = Mago('Mickey Mouse', 99, 'Walt Disney', 8000, 'Dinheiro')
lbj = Mago('Lebron James', 38, 'NBA', 90000, 'Basquete')
Thor = Mago('Thor', 1000, 'Mitologia Nórdica', 800, 'Trovão')


#Acessando atributos públicos
print(hp.nome)
print(hp.idade)
print(hp.escola)

#Invocando métodos
hp.andar()
hp.falar()
hp.invocarMagia()

gd.falar()

mm.verificar_elemento()
lbj.verificar_poder()
Thor.verificar_elemento()


del hp
del gd
del mm
del lbj
del Thor
