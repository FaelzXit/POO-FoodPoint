from models.pedido import Pedido
from models.produto import Produto

from database import (
    salvar_pedido,
    salvar_produto,
    listar_pedidos,
    listar_produtos,
    buscar_pedido,
    atualizar_pedido,
    deletar_pedido
)


produto1 = Produto("Hamburguer", 70)
produto2 = Produto("Batata Frita", 12)
produto3 = Produto("Refrizinho", 8)

salvar_produto(produto1)
salvar_produto(produto2)
salvar_produto(produto3)

produtos_banco = listar_produtos()

print(produtos_banco)

produtos = [produto1, produto2, produto3]


pedido1 = Pedido(5, "Separação", produtos)


pedido1.mostrarPedido()

print(pedido1.tempo)
print(pedido1.etapa)


id_pedido = salvar_pedido(pedido1)

print(id_pedido)

atualizar_pedido("Preparo", id_pedido)

pedido = buscar_pedido(id_pedido)

print(pedido)

deletar_pedido(id_pedido)

pedidos = listar_pedidos()

print(pedidos)