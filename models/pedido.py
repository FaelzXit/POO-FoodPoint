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
        self.tempo = novo_tempo

    def somar_produtos(self):
        soma = 0

        for produto in self.produtos:
            soma += produto.valor

        return soma