
#Questão 1-A)
class Pizza:

    def __init__(self,nome=str,categoria=str,tipo=str,ingredientes=str) -> None:
        self.nome = nome
        self.categoria = categoria
        self.tipo = tipo
        self.ingredientes = ingredientes
    
    def imprimirsabor(self):
        print([self.nome,self.categoria,self.tipo,self.ingredientes])

class PizzaPedido:

    def __init__(self,tamanho=str,nro_sabores=int,lista_sabores=list,status=str) -> None:
        self.tamanho = tamanho
        self.nro_sabores = nro_sabores
        self.lista_sabores = lista_sabores
        self.status = status
    
    def imprimirPizzaPedido(self):
        print(self.tamanho,self.nro_sabores,self.lista_sabores,self.status)

class SistemaPedidos:

    def __init__(self,catalogo,listadepedidos) -> None:
        self.catalogo = []
        self.listadepedidos = []
        
    def Adicionar_pedido(self):
        linha = 0
        for l in range(len(self.listadepedidos)):
            linha += 1
        pedido = [linha]
        sabores = []
        tamanho = input("Tamanho da Pizza(P,M,G): ")
        pedido.append(tamanho)
        if tamanho == 'P' or 'p':
            possibilidades = 2
        elif tamanho == 'M' or 'm':
            possibilidades = 3
        elif tamanho == 'G' or 'G':
            possibilidades = 4
        for a in range(possibilidades,0,-1):  
            sabores.append(input(self.catalogo,'\n',f"Escolha {a} sabores (salgado e doce não se misturam): "))
        pedido.append(sabores)
        pedido = PizzaPedido(tamanho,possibilidades,sabores,'Em preparo')
        self.listadepedidos.append(pedido)

    def Exibir_Catalogo(self):
        print(self.catalogo)

    def Exibir_status_do_pedido(self):
        n_pedido = input("Número do Pedido: ")
        status = self.listaDePedidos[n_pedido][0]
        print(status)
    
    def AlterarStatusPedido(self,n_pedido,novo_status):
        self.listaDePedidos[n_pedido][4] = novo_status

    def Exibir_Lista_de_Pedidos(self):
        print(self.listadepedidos)

#Questão 1-B)   

listaParaCatalogo = [
    ['Margherita', 'Salgada', 'Vegetariana', 'Muçarela, Tomate, Manjericão'],
    ['Pepperoni', 'Salgada', 'Com Carne', 'Pepperoni, Muçarela'],
    ['Quatro Queijos', 'Salgada', 'Vegetariana', 'Muçarela, Gorgonzola, Parmesão, Provolone'],
    ['Portuguesa', 'Salgada', 'Com Carne', 'Presunto, Muçarela, Ovo, Ervilhas, Azeitonas'],
    ['Calabresa', 'Salgada', 'Com Carne', 'Calabresa, Muçarela'],
    ['Frango com Catupiry', 'Salgada', 'Com Carne', 'Frango, Catupiry, Muçarela'],
    ['Banana Caramelizada', 'Doce', 'Vegetariana', 'Banana, Creme de Leite Condensado, Canela'],
    ['Chocolate com Morango', 'Doce', 'Vegetariana', 'Chocolate, Morango'],
    ['Vegetariana', 'Salgada', 'Vegetariana', 'Milho, Ervilhas, Pimentão, Tomate Cereja, Muçarela'],
    ['Supreme', 'Salgada', 'Com Carne', 'Pepperoni, Calabresa, Muçarela, Cebola, Pimentão, Azeitonas']
]

pizzas = []
for l in range(len(listaParaCatalogo)):
    pizzas.append(Pizza(listaParaCatalogo[l][0],listaParaCatalogo[l][1],listaParaCatalogo[l][2],listaParaCatalogo[l][3]))
for pizza in pizzas:
    pizza.imprimirsabor()

#Questão 1-C)

pedidosParaTestar = [
    [1, 'M', 2, ['Margherita', 'Calabresa'], 'Entregue'],
    [2, 'P', 2, ['Banana Caramelizada', 'Chocolate com Morango'], 'Pronto'],
    [3, 'G', 3, ['Vegetariana', 'Supreme', 'Pepperoni'], 'Entregue'],
    [4, 'P', 1, ['Frango com Catupiry'], 'Em preparo'],
    [5, 'G', 4, ['Quatro Queijos', 'Frango com Catupiry', 'Portuguesa', 'Bacon'], 'Pronto'],
    [6, 'M', 3, ['Margherita', 'Calabresa', 'Pepperoni'], 'Em preparo'],
    [7, 'G', 1, ['Bacon'], 'Recebido'],
    [8, 'P', 2, ['Margherita', 'Calabresa'], 'Em preparo'],
    [9, 'G', 2, ['Mussarela', 'Portuguesa'], 'Em preparo'],
    [10, 'M', 3, ['Quatro Queijos', 'Margherita', 'Frango com Catupiry'], 'Recebido']
]

listapedidos = []
for l in range(len(pedidosParaTestar)):
    listapedidos.append(l+1)
    listapedidos.append(PizzaPedido(pedidosParaTestar[l][1],pedidosParaTestar[l][2],pedidosParaTestar[l][3],pedidosParaTestar[l][4]))
    
sistema = SistemaPedidos(pizzas,listapedidos)
