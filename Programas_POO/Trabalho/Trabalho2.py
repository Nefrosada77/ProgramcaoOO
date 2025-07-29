import os
import csv
class Perfil:

    def __init__(self,nome,idade,lista_fav = list,lista_ult_assistidos = list) -> None:
        self.nome = nome
        self.idade = idade
        self.Fav = []
        if lista_fav == None:
            pass
        else:
            self.Fav.append(lista_fav)
        self.ult_ass = []
        if lista_ult_assistidos == None:
            pass
        else:
            self.ult_ass.append(lista_ult_assistidos)

    def add_fav(self,id_midia):
        if len(self.Fav) < 5:
            for midia in cat.lista_serie:
                if id_midia == midia.Get_Id():
                    self.Fav.append(midia.Get_Nome())
                else:
                    pass
            for midia in cat.lista_filmes:
                if id_midia == midia.Get_Id():
                    self.Fav.append(midia.Get_Nome())
                else:
                    pass
            for midia in cat.lista_documentarios:
                if id_midia == midia.Get_Id():
                    self.Fav.append(midia.Get_Nome())
                else:
                    pass  
            for midia in cat.lista_animacoes:
                if id_midia == midia.Get_Id():
                    self.Fav.append(midia.Get_Nome())
                else:
                    pass
            for midia in cat.lista_programas_tv:
                if id_midia == midia.Get_Id():
                    self.Fav.append(midia.Get_Nome())
                else:
                    pass  
        else:
            print("Limite de favoritos")
            input("...")
            #VOLTAR AO MENU

    def del_fav(self,id_midia):
        if len(self.Fav) != 0:
            for c in range(len(self.Fav)):
                for midia in cat.lista_serie:
                    if midia.Get_Nome() == self.Fav[c] and midia.Get_Id() == id_midia:
                        self.Fav.pop(c)
                    else:
                        pass
                for midia in cat.lista_filmes:
                    if midia.Get_Nome() == self.Fav[c] and midia.Get_Id() == id_midia:
                        self.Fav.pop(c)
                    else:
                        pass
                for midia in cat.lista_documentarios:
                    if midia.Get_Nome() == self.Fav[c] and midia.Get_Id() == id_midia:
                        self.Fav.pop(c)
                    else:
                        pass  
                for midia in cat.lista_animacoes:
                    if midia.Get_Nome() == self.Fav[c] and midia.Get_Id() == id_midia:
                        self.Fav.pop(c)
                    else:
                        pass
                for midia in cat.lista_programas_tv:
                    if midia.Get_Nome() == self.Fav[c] and midia.Get_Id() == id_midia:
                        self.Fav.pop(c)
                    else:
                        pass  
                
        else:
            print("Nenhum favorito para ser removido")
            input("...")
            #VOLTAR AO MENU

    def assistir(self,id_midia):
            for midia in cat.lista_serie:
                if id_midia == midia.Get_Id():
                    if self.ult_ass == 5:
                        self.ult_ass.pop(4)
                    self.ult_ass.insert(0,midia.Get_Nome())    
                else:
                    pass
            for midia in cat.lista_filmes:
                if id_midia == midia.Get_Id():
                    if self.ult_ass == 5:
                        self.ult_ass.pop(4)
                    self.ult_ass.insert(0,midia.Get_Nome()) 
                else:
                    pass
            for midia in cat.lista_documentarios:
                if id_midia == midia.Get_Id():
                    if self.ult_ass == 5:
                        self.ult_ass.pop(4)
                    self.ult_ass.insert(0,midia.Get_Nome()) 
                else:
                    pass  
            for midia in cat.lista_animacoes:
                if id_midia == midia.Get_Id():
                    if self.ult_ass == 5:
                        self.ult_ass.pop(4)
                    self.ult_ass.insert(0,midia.Get_Nome()) 
                else:
                    pass
            for midia in cat.lista_programas_tv:
                if id_midia == midia.Get_Id():
                    if self.ult_ass == 5:
                        self.ult_ass.pop(4)
                    self.ult_ass.insert(0,midia.Get_Nome()) 
                else:
                    pass          
    
    def listar_midias(self,user):
        if self.idade >= '18':
                for serie in cat.lista_serie:
                    print(serie.exibir_info())
                for filme in cat.lista_filmes:
                    print(filme.exibir_info())
                for doc in cat.lista_documentarios:
                    print(doc.exibir_info())
                for animacao in cat.lista_animacoes:
                    print(animacao.exibir_info())
                for programa in cat.lista_programas_tv:
                    print(programa.exibir_info())
        elif self.idade < '18' and self.idade >= '14':
                for serie in cat.lista_serie:
                    if serie.Get_classificacao() == '14':
                        print(serie.exibir_info())
                    else:
                        pass
                for filme in cat.lista_filmes:
                    if filme.Get_classificacao() == '14':
                        print(filme.exibir_info())
                    else:
                        pass
                for doc in cat.lista_documentarios:
                    if doc.Get_Classificacao() == '14':
                        print(doc.exibir_info())
                    else:
                        pass
                for animacao in cat.lista_animacoes:
                    if animacao.Get_Classificacao() == '14':
                        print(animacao.exibir_info())
                    else:
                        pass
                for programa in cat.lista_programas_tv:
                    if programa.Get_Classificacao() == '14':
                        print(programa.exibir_info())
                    else:
                        pass                    
        elif self.idade < '14' and self.idade >= '10':
                for serie in cat.lista_serie:
                    if serie.Get_classificacao() == '10':
                        print(serie.exibir_info())
                    else:
                        pass
                for filme in cat.lista_filmes:
                    if filme.Get_classificacao() == '10':
                        print(filme.exibir_info())
                    else:
                        pass
                for doc in cat.lista_documentarios:
                    if doc.Get_Classificacao() == '10':
                        print(doc.exibir_info())
                    else:
                        pass
                for animacao in cat.lista_animacoes:
                    if animacao.Get_Classificacao() == '10':
                        print(animacao.exibir_info())
                    else:
                        pass
                for programa in cat.lista_programas_tv:
                    if programa.Get_Classificacao() == '10':
                        print(programa.exibir_info())
                    else:
                        pass                                   
        elif self.idade > '10':
                for serie in cat.lista_serie:
                    if serie.Get_classificacao() == 'L':
                        print(serie.exibir_info())
                    else:
                        pass
                for filme in cat.lista_filmes:
                    if filme.Get_classificacao() == 'L':
                        print(filme.exibir_info())
                    else:
                        pass
                for doc in cat.lista_documentarios:
                    if doc.Get_Classificacao() == 'L':
                        print(doc.exibir_info())
                    else:
                        pass
                for animacao in cat.lista_animacoes:
                    if animacao.Get_Classificacao() == 'L':
                        print(animacao.exibir_info())
                    else:
                        pass
                for programa in cat.lista_programas_tv:
                    if programa.Get_Classificacao() == 'L':
                        print(programa.exibir_info())
                    else:
                        pass                    
        midia = input("Selecionar midia(ID): ")
        for serie in cat.lista_serie:
            if midia == serie.id:
                serie.menu_midia(self,user)
            else:
                pass
        for filme in cat.lista_filmes:
            if midia == filme.id:
                filme.menu_midia(self,user)
        for doc in cat.lista_documentarios:
            if midia == doc.id:
                doc.menu_midia(self,user)
        for animacao in cat.lista_animacoes:
            if midia == animacao.id:
                animacao.menu_midia(self,user)
        for programa in cat.lista_programas_tv:
            if midia == programa.id:
                programa.menu_midia(self,user)

    def buscar_titulo(self,titulo):
        achou_titulo = False
        for object in cat.lista_serie:
            if object.Get_Nome() == titulo:
                print(object.exibir_info())
                achou_titulo = True
            else:
                pass
        for object in cat.lista_filmes:
            if object.Get_Nome() == titulo:
                print(object.exibir_info())
                achou_titulo = True
            else:
                pass  
        for object in cat.lista_documentarios:
            if object.Get_Nome() == titulo:
                print(object.exibir_info())
                achou_titulo = True
            else:
                pass
        for object in cat.lista_animacoes:
            if object.Get_Nome() == titulo:
                print(object.exibir_info)
                achou_titulo = True
            else:
                pass
        for object in cat.lista_programas_tv:
            if object.Get_Nome() == titulo:
                print(object.exibir_info)
                achou_titulo = True
            else:
                pass
        if achou_titulo == False:
            print("Titulo não encontrado")
            input("...")
        else:
            input("...")
            #VOLTAR AO MENU              
 
    def Get_Nome(self):
        return self.nome

    def Lista_fav(self):
        print(f"Favoritos de {self.nome}:")
        print(self.Fav)
        input("...")
        #VOLTAR AO MENU
    
    def Lista_ult(self):
        print("Ultimos Assistidos: ")
        print(self.ult_ass)
        input("...")
        #VOLTAR AO MENU

    def menu_Net(self,user):
        e = 0
        while e != 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1 - Buscar por nome")
            print("2 - Histórico")
            print("3 - Favoritos")
            print("4 - Listar Midias")
            print("5 - Voltar ao Menu Anterior")
            e = int(input("Escolha uma opção: "))
            if e == 1:
                titulo = input("Titulo do filme: ")
                self.buscar_titulo(titulo)
            if e == 2:
                self.Lista_ult()
            if e == 3:
                self.Lista_fav()
            if e == 4:
                self.listar_midias(user)
            if e == 5:
                user.menu_perfil()

class usuario:

    def __init__(self,nome,senha,IsPremium = bool) -> None:
        self.lista_perfil = []
        self.nome = nome  
        self.senha = senha
        self.premium = IsPremium
        pers = open('Perfis.csv', '+r')
        lista_perfis = csv.reader(pers)
        for row in lista_perfis:
            if row[0] == self.nome:
                self.lista_perfil.append(Perfil(row[1],row[2],row[3],row[4]))
            else:
                pass
    
    def Get_nome(self):
        return self.nome
    
    def Get_senha(self):
        return self.senha
    
    def menu_perfil(self):
        e = 0
        while e != 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            for pref in self.lista_perfil:
                print(f"Perfis: {pref.nome}")
            print("0 - Alterar Assinatura")
            print("1 - Acessar Perfil")
            print("2 - Editar Perfil")
            print("3 - Adicionar Perfil")
            print("4 - Remover Perfil")
            print("5 - Voltar ao Menu Anterior")
            e = int(input("Escolha uma opção: "))
            if e == 0:
                self.alt_plano()
            if e == 1:
                perfil = input("Perfil Acessado: ")
                for perf in self.lista_perfil:
                    if perf.nome == perfil:
                        perf.menu_Net(self)
                    else:
                        pass
            if e == 2:
                self.alt_senha()
            if e == 3:
                self.add_perfil()
            if e == 4:
                self.del_perfil()
            if e == 5:
                menu_iniciar()

    def add_perfil(self):
        if self.premium == True:
            if len(self.lista_perfil) < 5:
                nome = input("Nome do Perfil: ")
                idade = input("Idade do Perfil: ")
                self.lista_perfil.append(Perfil(nome,idade,None,None))
                input("...")
                #VOLTAR AO MENU
            else:
                print("Número de Perfis excedido")
                input("...")
                #VOLTAR AO MENU
        else:
            if len(self.lista_perfil) < 3:
                nome = input("Nome do Perfil: ")
                idade = input("Idade do Perfil: ")
                self.lista_perfil.append(Perfil(nome,idade,None,None))
                input("...")
                #VOLTAR AO MENU
            else:
                print("Número de Perfis excedido")
                input("...")
                #VOLTAR AO MENU

    def del_perfil(self):
        nome = input("Nome do Perfil: ")
        for perfil in self.lista_perfil:    
            if perfil.Get_Nome() == nome:
                self.lista_perfil.remove(perfil)

    def alt_senha(self):
        nova_senha = input("Digite nova senha: ")
        self.senha = nova_senha
        #VOLTAR AO MENU

    def alt_plano(self):
        if self.premium == True:
            if len(self.lista_perfil) > 3:
                print("É necessário deletar perfis")
                #VOLTAR AO MENU
            else:
                print("Trocando plano Premium para Simples")
                self.premium = False
                #VOLTAR AO MENU
        else:
            print("Trocando plano Simples para Premium")
            self.premium = True
            #COLTAR AO MENU

class midia:

    def ___init___(self) -> None:
        pass

    def exibir_info_midia(self):
        pass
    
class serie(midia):

    def __init__(self, id, tipo, titulo, genero, ano, classificacao,nro_temp,lista_ep_temp) -> None:
        super().__init__()
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.classificacao = classificacao
        self.nro_temp = nro_temp
        self.lista_ep_temp = lista_ep_temp

    def exibir_info(self):
        print(f"{self.id} - {self.tipo} - {self.titulo} - {self.genero} - {self.ano} - {self.classificacao}")
        print(f"Temporadas: {self.nro_temp}")
        #VOLTAR PARA O MENU
    
    def listar_episodios(self,temp):
        achou_temp = False
        for l in range(len(self.lista_ep_temp)):
            if self.lista_ep_temp[l][3] == (temp):
                print(self.lista_ep_temp[l])
                achou_temp = True
            else:
                pass
        if achou_temp == True:
            pass
        else:
            print("Temporada nao econtrada")
    
    def Get_Id(self):
        return self.id
    
    def Get_Nome(self):
        return self.titulo

    def Get_Classificacao(self):
        return self.classificacao

    def menu_midia(self,perfil,user):
        e = 0
        while e != 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_info()
            print("1 - Assistir")
            print("2 - Favoritar/desvatoritar")
            print("3 - Listar Episodios")
            print("4 - Voltar ao menu anterior")
            e = int(input("Escolha uma opção: "))
            if e == 1:
                perfil.assistir(self.id)
                perfil.menu_Net(user)
            if e == 2:
                if self.titulo in perfil.Fav:
                    perfil.del_fav(self.id)
                else:
                    perfil.add_fav(self.id)
                perfil.menu_Net(user)
            if e == 3:
                temp = input("Seleciona a Temporada: ")
                self.listar_episodios(temp)
                input("...")
                perfil.menu_Net(user)
            if e == 4:
                perfil.menu_Net(user)

class filme(midia):

    def __init__(self, id, tipo, titulo, genero, ano, classificacao,director,producer) -> None:
        super().__init__()
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.classificacao = classificacao
        self.director = director
        self.producer = producer

    def exibir_info(self):
        print(f"{self.id} - {self.tipo} - {self.titulo} - {self.genero} - {self.ano} - {self.classificacao}")
        print(f"Diretor: {self.director}\nProdutor: {self.producer}")
        #VOLTAR PARA O MENU

    def Get_Id(self):
        return self.id
    
    def Get_Nome(self):
        return self.titulo

    def Get_Classificacao(self):
        return self.classificacao
    
    def menu_midia(self,perfil,user):
        e = 0
        while e != 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_info()
            print("1 - Assistir")
            print("2 - Favoritar/desvatoritar")
            print("3 - Voltar ao menu anterior")
            e = int(input("Escolha uma opção: "))
            if e == 1:
                perfil.assistir(self.id)
                perfil.menu_Net(user)
            if e == 2:
                if self.titulo in perfil.Fav:
                    perfil.del_fav(self.id)
                else:
                    perfil.add_fav(self.id)
                perfil.menu_Net(user)
            if e == 3:
                perfil.menu_Net(user)
            
class documentario(midia):
    
    def __init__(self, id, tipo, titulo, genero, ano, classificacao,tema) -> None:
        super().__init__()
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.classificacao = classificacao
        self.tema = tema

    def exibir_info(self):
        print(f"{self.id} - {self.tipo} - {self.titulo} - {self.genero} - {self.ano} - {self.classificacao}")
        print(f"Tema: {self.tema}")
        #VOLTAR PARA O MENU

    def Get_Id(self):
        return self.id
    
    def Get_Nome(self):
        return self.titulo

    def Get_Classificacao(self):
        return self.classificacao

    def menu_midia(self,perfil,user):
        e = 0
        while e != 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_info()
            print("1 - Assistir")
            print("2 - Favoritar/desvatoritar")
            print("3 - Voltar ao menu anterior")
            e = int(input("Escolha uma opção: "))
            if e == 1:
                perfil.assistir(self.id)
                perfil.menu_Net(user)
            if e == 2:
                if self.titulo in perfil.Fav:
                    perfil.del_fav(self.id)
                else:
                    perfil.add_fav(self.id)
                perfil.menu_Net(user)
            if e == 3:
                perfil.menu_Net(user)
        
class animacao(midia):
    
    def __init__(self, id, tipo, titulo, genero, ano, classificacao,studio) -> None:
        super().__init__()
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.classificacao = classificacao
        self.studio = studio

    def exibir_info(self):
        print(f"{self.id} - {self.tipo} - {self.titulo} - {self.genero} - {self.ano} - {self.classificacao}")
        print(f"Estudio: {self.studio}")
        #VOLTAR PARA O MENU

    def Get_Id(self):
        return self.id
    
    def Get_Nome(self):
        return self.titulo

    def Get_Classificacao(self):
        return self.classificacao

    def menu_midia(self,perfil,user):
        e = 0
        while e != 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_info()
            print("1 - Assistir")
            print("2 - Favoritar/desvatoritar")
            print("3 - Voltar ao menu anterior")
            e = int(input("Escolha uma opção: "))
            if e == 1:
                perfil.assistir(self.id)
                perfil.menu_Net(user)
            if e == 2:
                if self.titulo in perfil.Fav:
                    perfil.del_fav(self.id)
                else:
                    perfil.add_fav(self.id)
                perfil.menu_Net(user)
            if e == 3:
                perfil.menu_Net(user)
    
class programa(midia):
    
    def __init__(self, id, tipo, titulo, genero, ano, classificacao,nro_ep,lista_ep) -> None:
        super().__init__()
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.classificacao = classificacao
        self.nro_ep = nro_ep
        self.lista_ep = lista_ep

    def exibir_info(self):
        print(f"{self.id} - {self.tipo} - {self.titulo} - {self.genero} - {self.ano} - {self.classificacao}")
        print(f"Número de episódios: {self.nro_ep}")

    def listar_ep(self): 
        print(self.lista_ep)

    def Get_Id(self):
        return self.id
    
    def Get_Nome(self):
        return self.titulo

    def Get_Classificacao(self):
        return self.classificacao

    def menu_midia(self,perfil,user):
        e = 0
        while e != 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_info()
            print("1 - Assistir")
            print("2 - Favoritar/desvatoritar")
            print("3 - Listar Episodios")
            print("4 - Voltar ao menu anterior")
            e = int(input("Escolha uma opção: "))
            if e == 1:
                perfil.assistir(self.id)
                perfil.menu_Net(user)
            if e == 2:
                if self.titulo in perfil.Fav:
                    perfil.del_fav(self.id)
                else:
                    perfil.add_fav(self.id)
                perfil.menu_Net(user)
            if e == 3:
                self.listar_ep()
                input("...")
                perfil.menu_Net(user)
            if e == 4:
                perfil.menu_Net(user)

class catalogo:

    def __init__(self):
        self.lista_serie = [] 
        self.lista_filmes = []
        self.lista_documentarios = []
        self.lista_animacoes = []
        self.lista_programas_tv = []

    def add_midia(self,id,tipo,titulo,genero,ano,classificacao,nro_temp,director,producer,tema,studio):
        match tipo:
            case "Serie":
                ep = open('Ep_Serie.csv', '+r')
                lista = csv.reader(ep)  
                lista_ep_temp = [['Nro','Serie','Titulo','Temporada']]
                for row in lista:
                    if row[1] == titulo:
                        lista_ep_temp.append(row)
                self.lista_serie.append(serie(id, tipo, titulo, genero, ano, classificacao,nro_temp,lista_ep_temp))
                ep.close()
            case "Filme":
                self.lista_filmes.append(filme(id, tipo, titulo, genero, ano, classificacao,director,producer))
            case "Documentario":
                self.lista_documentarios.append(documentario(id, tipo, titulo, genero, ano, classificacao,tema))
            case "Animacao":
                self.lista_animacoes.append(animacao(id, tipo, titulo, genero, ano, classificacao,studio))
            case "Programa":
                ep = open('Ep_Serie.csv', '+r')
                lista = csv.reader(ep)   
                lista_ep_temp = [['Nro','Serie','Titulo','Temporada']]
                for row in lista:
                    if row[1] == titulo:
                        lista_ep_temp.append(row)
                self.lista_programas_tv.append(programa(id, tipo, titulo, genero, ano, classificacao,nro_temp,lista_ep_temp))
                ep.close()
            

    def obter_lista(self):
        print("Tipos de Midia:")
        print("1 - Series")
        print("2 - Filmes")
        print("3 - Documentarios")
        print("4 - Animacoes")
        print("5 - Programas de TV")
        tipo = int(input("Tipo de Midia (nro): "))
        match tipo:
            case 1:
                for serie in self.lista_serie:
                    print(serie.exibir_info())
                input("...")
                #VOLTAR PARA O MENU
            case 2:
                for filme in self.lista_filmes:
                    print(filme.exibir_info())
                input("...")
                #VOLTAR PARA O MENU
            case 3:
                for doc in self.lista_documentarios:
                    print(doc.exibir_info())
                input("...")
                #VOLTAR PARA O MENU
            case 4:
                for animacao in self.lista_animacoes:
                    print(animacao.exibir_info())
                input("...")
                #VOLTAR PARA O MENU
            case 5:
                for programa in self.lista_programas_tv:
                    print(programa.exibir_info())
                input('...')
                #VOLTAR PARA O MENU
            case 6:
                for serie in self.lista_serie:
                    print(serie.exibir_info())
                for filme in self.lista_filmes:
                    print(filme.exibir_info())
                for doc in self.lista_documentarios:
                    print(doc.exibir_info())
                for animacao in self.lista_animacoes:
                    print(animacao.exibir_info())
                for programa in self.lista_programas_tv:
                    print(programa.exibir_info())
                input("...")

def menu_iniciar():
    e = 0
    while e != 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1- Acessar")
        print("2- Criar Conta")
        print("3- Sair")
        e = int(input("Escolha uma opção: "))
        if e == 1:
            nome = input("Nome: ")
            senha = input("Senha: ")
            for user in Usuarios:
                if user.Get_nome() == nome and user.Get_senha() == senha:
                    user.menu_perfil()
                else:
                    pass
        if e == 2:
            nome = str(input("Nome: "))
            senha = str(input("Senha: "))
            Premium = int(input("1-Simples\n2-Premium\nPlano: "))
            if Premium == 1:
                isPremium = False
            elif Premium == 2:
                isPremium = True
            Usuarios.append(usuario(nome,senha,isPremium))


cat = catalogo()
lista = open('CatalogoGeral.csv','r+')
midi = csv.reader(lista)
for row in midi:
    cat.add_midia(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])

Usuarios = []
usu = open('Usuarios.csv', 'r+')
usuar_io = csv.reader(usu)
for row in usuar_io:
    Usuarios.append(usuario(row[0],row[1],row[2]))

menu_iniciar()