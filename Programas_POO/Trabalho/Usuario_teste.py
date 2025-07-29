import csv

class Album:
    def __init__(self):
        self.figurinhas = [False,False,False,False,False,False,False,False,False,False]
        self.requsicoesTrocas = []
    
    def colarFigurinha(self, nro):
        self.figurinhas[nro] = True

    def possuiFigurinha(self, nro):
        if self.figurinhas[nro] == True:
            return True
        else:
            return False


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha= senha
        self.album= Album()
        self.colecao = [0,0,0,0,0,0,0,0,0,0]
    
    def adicionarFigurinhaColecao(self, nro):
        self.colecao[nro] =  self.colecao[nro] + 1

    def colarFigurinhaAlbum(self, nro):
        self.album.colarFigurinha(nro)

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

class Figurinha:
    def __init__(self):
        pass

class Trocas:
    def __init__(self):
        pass


usuarios = [] 
trocas = [] 
infosFigurinhas = [] 



f = open('Usuario.csv', 'r+')
reader = csv.reader(f)
for row in reader:
    usuarios.append(Usuario(row[0],row[1]))
  
