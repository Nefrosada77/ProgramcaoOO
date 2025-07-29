import csv
import os
import random
def menu_inicial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1 - Novo álbum")
    print("2 - Acessar álbum")
    print("3 - Sair do aplicativo")
    escolha = int(input("Opção escolhida: "))
    if escolha == 1:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        usuarios.append(Usuario(usuario,senha))
        menu2(usuarios[len(usuarios)])

    elif escolha == 2:
        usuario = input("Usuário: ")
        senha = input("Senha: ")   
        for user in usuarios:
            user.Autorizar_Login(usuario,senha)



    elif escolha == 3:
        pass


def menu2(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1 - Ver álbum")
    print("2 - Gerenciar a coleção")
    print("3 - Abrir pacote de figurinhas")
    print("4 - Volte ao menu anterior")
    escolha = int(input("Opção escolhida: "))
    if escolha == 1:
        user.mostrarAlbum()
        menu2(user)
        
    elif escolha == 2:
        menu_colecao(user)

    elif escolha == 3:
        user.AbrirPack()
        menu2(user)

    elif escolha == 4:
        menu_inicial()


def menu_colecao(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1 - Colar figurinha")
    print("2 - Disponibilizar para troca")
    print("3 - Propor troca de figurinhas")
    print("4 - Revisar solicitações de troca")
    print("5 - Voltar ao menu anterior")
    escolha = int(input("Opção escolhida: "))
    if escolha == 1:
        for nro in infosFigurinhas:
            print(f"#{nro.GetNro()} - {nro.GetNome()}")
        nro = int(input("Digite o número da figurinha: "))
        user.colarFigurinhaAlbum(nro)
        menu_colecao(user)


    elif escolha == 2:
        pass

    elif escolha == 3:
        for users in usuarios:
            users.PrintAlbum()
        user2 = input("Usuario para trocar: ")
        nro1 = int(input("Figurinha para ser trocada: "))
        nro2 = int(input("Figurinha Recebida: "))
        trocas.append(Trocas(user.getNome(),user2,nro1,nro2))

    elif escolha == 4:
        for troca in trocas:
            troca.PrintFigurinha(user)
        confirm = input("Realizar troca(S/N):")
        if confirm == 'S' or 's':
            troca = input("Digite o número da troca: ")
            trocas[troca].RealizarTroca(troca)
        else:
            menu_colecao(user)
        

    elif escolha == 5:
        menu2(user)

        
class Album:
    def __init__(self):
        self.figurinhas = [False,False,False,False,False,False,False,False,False,False]
        self.requsicoesTrocas = []
    
    def colarFigurinha(self, nro):
        if self.figurinhas[nro] == True:
            input("Figurinha já colada...")
        else:
            self.figurinhas[nro] = True

    def possuiFigurinha(self, nro):
        if self.figurinhas[nro] == True:
            return True
        else:
            return False
    
    def PrintAlbum(self):
        print(self.figurinhas)


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha= senha
        self.album= Album()
        self.colecao = [0,0,0,0,0,0,0,0,0,0]
    
    def adicionarFigurinhaColecao(self, nro):
        self.colecao[nro] =  self.colecao[nro] + 1

    def colarFigurinhaAlbum(self, nro):
        if self.colecao[nro] == 0:
            pass
        else:
            self.album.colarFigurinha(nro)
        self.colecao[nro] -= 1
        menu2(self)

    def getNome(self):
        return self.nome

    def getAlbum(self):
        return self.album
    
    def possuiFigurinhaNoAlbum(self, nro):
        return self.album.possuiFigurinha(nro)
    
    def possuiFigurinhaNaColecao(self, nro):
        if self.colecao[nro] > 0:
            return True
        else:
            return False
    
    def Autorizar_Login(self, usuario, senha):
        if usuario == self.nome and senha == self.senha:
            menu2(self)
        else:
            pass
        
    def PrintAlbum(self):
        self.album.PrintAlbum()

    def AbrirPack(self):

        Pack = [0,1,2,3,4,5,6,7,8,9]
        print("Figurinhas Retiradas:")
        for i in range(3):
            figurinhasescolhidas = random.choice(Pack)
            print(figurinhasescolhidas)
            self.adicionarFigurinhaColecao(figurinhasescolhidas)
        input('Continuar...')
            
    def mostrarAlbum(self):
        print("Album de",self.nome)
        for item in range(len(self.colecao)):
            if self.possuiFigurinhaNoAlbum(item) == True and self.possuiFigurinhaNaColecao(item) >= 1:
                print("Nº",item,"-",self.colecao[item],"- status: 2")
            elif self.possuiFigurinhaNoAlbum(item) == True and self.possuiFigurinhaNaColecao(item) == 0:
                print("Nº",item,"-",self.colecao[item],"- status: 1")
            elif self.possuiFigurinhaNoAlbum(item) == False and self.possuiFigurinhaNaColecao(item) >= 1:
                print("Nº",item,"-",self.colecao[item],"- status: 0")
        input('Continuar...')
    
    def DiminuirColecao(self,nro):
        self.colecao[nro] -= 1

    def AumentarColecao(self,nro):
        self.colecao[nro] += 1
                

class Figurinha:
    def __init__(self,nome,numero):

        self.nome = nome
        self.numero = numero


    
    def GetNome(self):
        return self.nome
    
    def GetNro(self):
        return self.numero
    


class Trocas:
    def __init__(self,user1,user2,nro1,nro2):
        self.user1 = user1
        self.user2 = user2
        self.nro1 = int(nro1)
        self.nro2 = int(nro2)

    def PrintFigurinha(self):
        for user in usuarios:
            if self.user1 == user.GetNome():
                ntroca = 0
                print(ntroca,self.user1,'-', self.nro1,'->',self.user2,'-',self.nro2)
            else:
                pass
    
    def RealizarTroca(self,user):
        user.DiminuirColecao(self.nro1)
        for users in usuarios:
            if self.user2 == users.GetNome:
                users.DiminuirColecao(self.nro2)

      

usuarios = [] 
trocas = [] 
infosFigurinhas = [] 

f = open('Usuario.csv', 'r+')
reader = csv.reader(f)
for row in reader:
    usuarios.append(Usuario(row[0],row[1]))
f.close()

v = open('Figurinhas.csv', 'r+')
leitor = csv.reader(v)
for item in leitor:
    infosFigurinhas.append(Figurinha(item[1],item[0]))
v.close()


t = open('Trocas.csv', 'r+')
reader = csv.reader(t)
for row in reader:
    trocas.append(Trocas(row[0],row[1],row[2],row[3]))
t.close()


menu_inicial()