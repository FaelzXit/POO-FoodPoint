from models.pedido import Pedido
from models.produto import Produto


def criar_pedido(dados_formulario):
    produtos = []

    for numero in range(1, 4):
        nome = dados_formulario.get("item_" + str(numero), "").strip()
        valor = dados_formulario.get("valor_" + str(numero), "").strip()
        valor = valor.replace(",", ".")

        if nome == "" and valor == "":
            continue

        if nome == "" or valor == "":
            return None, "Preencha o nome e o valor de cada produto."

        try:
            valor = float(valor)
        except ValueError:
            return None, "Informe um valor válido para cada produto."

        if not 0 < valor <= 99999.99:
            return None, "Informe um valor entre R$ 0,01 e R$ 99.999,99."

        if len(nome) > 80:
            return None, "O nome do produto pode ter até 80 caracteres."

        produto = Produto(nome, valor)
        produtos.append(produto)

    if len(produtos) == 0:
        return None, "Adicione pelo menos um produto ao pedido."

    pedido = Pedido(0, "Separação", produtos)
    return pedido, None
