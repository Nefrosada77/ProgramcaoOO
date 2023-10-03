class CadastroCliente:

    def __init__(self) -> None:
        pass

    def Cadastrar(self):
        self.nome = input("Nome: ")
        self.sobrenome = input("Sobrenome: ")
        self.datanac = input("Data de Nascimento: ")
        self.email = input("E-mail: ")
        self.CPF = input("CPF: ")
        self.senha = input("Senha: ")

    def Consultar_Dados(self):
        tentativas = 0
        while tentativas != 3:
            tEmail = input("Email: ")
            tsenha = input("Senha: ")
            if tEmail != self.email or tsenha != self.senha:
                tentativas += 1
        if tentativas >= 3:
            input("Cadastro Bloqueada...")
        else:
            print("Nome:",self.nome)
            print("Sobrenome:",self.sobrenome)
            print("Data de Nascimento:",self.datanac)
            print("E-mail:",self.email)
            print("CPF:",self.CPF)
            print("Senha:",self.senha)
        
Vinicius = CadastroCliente()
Vinicius.Cadastrar()
Vinicius.Consultar_Dados()