class Data:
    
    #Método construtor
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprimirData(self):
        print(self.dia,'/',self.mes,'/',self.ano)

    def imprimirDataPorExtenso(self,cidade):

        strmes = self.mes

        match strmes:
            case 1:
                strmes = 'Janeiro'
            case 2:
                strmes = 'Fevereiro'
            case 3:
                strmes = 'Marco'
            case 4:
                strmes = 'Abril'
            case 5:
                strmes = 'Maio'
            case 6:
                strmes = 'Junho'
            case 7:
                strmes = 'Julho'
            case 8:
                strmes = 'Agosto'
            case 9:
                strmes = 'Setembro'
            case 10:
                strmes = 'Outubro'
            case 11:
                strmes = 'Novembro'
            case 12:
                strmes = 'Dezembro'
        print(cidade,' , ',self.dia, ' de ', strmes, ' de ', self.ano)    

data = Data(24,8,2023)

data.imprimirData()
data.imprimirDataPorExtenso('Porto Alegre')