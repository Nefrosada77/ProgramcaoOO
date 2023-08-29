import csv
import os

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1- Visualizar base de dados")
    print("2- Montar uma playlist")
    print("3- Visualizar a playlist")
    print("4- Embaralhar a playlist")
    print("5- Duração da playlist")
    print("6- Consultar música")
    print("7- Consultar por banda/artista")
    print("8- Sair")

#MATRIZ ONDE SERÁ GUARDADA A PLAYLIST
Playlist = [['ID',	'Nome',	                'Artista',	                    'Genero',	    'Ano',	    'Duracao']]

#MATRIZ ONDE SERÁ GUARDADA A BASE DE DADOS
Base = []

#-----------------#
escolha = 0
#-----------------#

print("Deeznuts")
while escolha != 8:
    menu()
    escolha = int(input("Selecione uma das opções: "))
#- Visualizar base de dados: se escolhida esta opção, o programa deve mostrar ao usuário a tabela com todas as músicas -#
    if escolha == 1:
        f = open('BaseDadosPlaylist.csv', 'r+')
        reader = csv.reader(f)
        Base = list(list(reader))
        for l in range(len(Base)):
            for c in range(len(Base[0])):
                print(f"{Base[l][c]}-", end='')
            print()
        print() 
        input("Pressione ENTER para continuar...")

#- Montar uma playlist: quando o usuário escolher esta opção, o programa deve permitir, enquanto ele quiser, adicionar músicas da base de dados. Para isso, o usuário deve fornecer um ID válido da música do banco de dados e este ID deve ser armazenado na lista. Atenção! Só poderão ser adicionadas músicas que não estejam na playlist. -#   
    if escolha == 2:
        musica_escolhida = input("Coloque o ID para adcionar a música desejada: ")
        for l in range(len(Base)):        
            if musica_escolhida in Base[l][0]:
                prossiga = 1       

        for l in range(len(Playlist)):
            if musica_escolhida in Playlist[l][0]:
                prossiga = 0

        if prossiga == 1:
            for l in range(len(Base)):
                if Base[l][0] == musica_escolhida:
                    Playlist.append(Base[l])                                    
            for y in range(len(Playlist)):
                for x in range(len(Playlist[0])):
                    print(f"{Playlist[y][x]}-", end='')
                print() 
            print()        
            input("Pressione ENTER para continuar...")
            prossiga = 0
        
        else:
            print("ID Inválido")
            print()        
            input("Pressione ENTER para continuar...")    
               
#- Visualizar a playlist: se escolhida esta opção, o programa deve mostrar apenas as informações a respeito das músicas da playlist. -#
    if escolha == 3:
        for y in range(len(Playlist)):
            for x in range(len(Playlist[0])):
                print(f"{Playlist[y][x]} ", end='')
            print()
        print()
        input("Pressione ENTER para continuar...")

#- Embaralhar playlist: se escolhida esta opção, o programa deve embaralhar a ordem das músicas da playlist e exibir o resultado. -#
    if escolha == 4:
        pass

#- Mostrar a duração total da playlist, em minutos -#    
    if escolha == 5:
        duracao = 0
        for y in range(len(Playlist)):
            if y == 0:
                pass
            else:
                numero = int(Playlist[y][5])
                duracao += numero
        print(f"Duração da Playlist: {duracao} Minutos")
        print()
        input("Pressione ENTER para continuar...")
             
#- Consultar música: o usuário entra com o título da música e o programa retorna o ID da música no banco de dados, se houver -#
    if escolha == 6:
        pass

#- Consultar por banda/artista: usuário entra com o nome da banda/artista e o programa retorna a lista da(s) ID(s) das música(s) encontradas, se houver. -#
    if escolha == 7:
        pass

#- Sair -#
    if escolha == 8:
        break