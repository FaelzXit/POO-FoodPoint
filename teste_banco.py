
from models.pedido import Pedido
from models.produto import Produto

from database import (
    salvar_pedido,
    salvar_produto,
    listar_pedidos,
    listar_produtos,
    listar_produtos_do_pedido,
    buscar_pedido,
    atualizar_pedido,
    deletar_pedido
)


print("========== INICIANDO TESTES ==========")


produto1 = Produto("Hamburguer", 70)
produto2 = Produto("Batata Frita", 12)
produto3 = Produto("Refrizinho", 8)

produtos = [produto1, produto2, produto3]


for produto in produtos:
    salvar_produto(produto)

print("\n========== TODOS OS PRODUTOS ==========")
print(listar_produtos())


pedido1 = Pedido(5, "Separação", produtos)
id_pedido = salvar_pedido(pedido1)

print("\n========== CADASTRO DO PEDIDO ==========")
print(buscar_pedido(id_pedido))


print("\n========== PRODUTOS DO PEDIDO ==========")
print(listar_produtos_do_pedido(id_pedido))


atualizar_pedido("Preparo", id_pedido)

print("\n========== PEDIDO ATUALIZADO ==========")
print(buscar_pedido(id_pedido))


print("\n========== TODOS OS PEDIDOS ==========")
print(listar_pedidos())


deletar_pedido(id_pedido)

print("\n========== PEDIDOS APÓS EXCLUSÃO ==========")
print(listar_pedidos())


print("\n========== FIM DOS TESTES ==========")
