class Pessoa():
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def mostrar_dados(self):
        print("nome: ", self.nome)
        print("idade: ", self.idade)
        print("email: ", self.email)
        
        
class Gestor(Pessoa):

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Email:", self.email)
        print("Função Gestor")


gestor1 = Gestor("Rafael", 18, "rafael@gmail.com")

print(gestor1.nome)
print(gestor1.idade)
print(gestor1.email)

gestor1.mostrar_dados()



class Produto:
    def __init__(self, item, valor):
        self.item = item
        self.valor = valor


produto1 = Produto("Hamburguer", 70)
produto2 = Produto("Batata Frita", 12)
produto3 = Produto("Refrizinho", 8)

produtos = [produto1, produto2, produto3]


class Pedido:
    def __init__(self, tempo, etapa, produtos):
        self.tempo = tempo
        self.etapa = etapa
        self.produtos = produtos    

    def mostrarPedido(self):
        print("Tempo:", self.tempo)
        print("Etapa:", self.etapa)

        for produto in self.produtos:
            print("Produto:", produto.item)
            print("Valor:", produto.valor)

    def alterar_etapa(self, nova_etapa):
        self.etapa = nova_etapa
        
    def alterar_tempo(self, novo_tempo):
        self.tempo = novo_tempo;
        
    def somar_produtos(self):
        
        soma = 0
        
        for produto in self.produtos:
            soma += produto.valor
        return soma
        

pedido1 = Pedido(5, "Separação", produtos)
pedido1.alterar_tempo(10)

pedido1.mostrarPedido()
print(pedido1.somar_produtos())