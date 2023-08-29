class Musica:
    Playlist = []

    def __init__(self, ID, Nome, Artista,Genero, Ano, Duracao):
        self.ID = ID
        self.Nome = Nome
        self.Artista = Artista
        self.Genero = Genero
        self.Ano = Ano
        self.Duracao = Duracao

    def Visualizar_Base(self):
        print(self.ID,' - ',self.Nome,' - ',self.Artista,' - ',self.Genero,' - ',self.Ano,' - ',self.Duracao)

    def Adicionar_Playlist(self):
        a = input(f"Adicionar: {self.Nome}?\n('S' para sim / 'N' para não)\n")
        if a == 'S':
            Musica.Playlist.append(self.Nome)
            print(Musica.Playlist)
        else:
            print(Musica.Playlist)


Roses = Musica(1,'Roses','Kanye West','Hip-Hop',2005,4)
Chase = Musica(2,'Chase','batta','Rock',2016,3)
Grimm = Musica(3,'The Grimm Troupe','Christopher Larkin','Jazz',2017,2)

Roses.Visualizar_Base()
Chase.Visualizar_Base()
Grimm.Visualizar_Base()

Roses.Adicionar_Playlist()
Chase.Adicionar_Playlist()
Grimm.Adicionar_Playlist()