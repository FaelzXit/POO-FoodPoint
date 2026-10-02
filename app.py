from models.pedido import Pedido
from models.produto import Produto

produto1 = Produto("Hamburguer", 70)
produto2 = Produto("Batata Frita", 12)
produto3 = Produto("Refrizinho", 8)

produtos = [produto1, produto2, produto3]

pedido1 = Pedido(5, "Separação", produtos)

print(pedido1.tempo)
print(pedido1.etapa)

pedido1.mostrarPedido()