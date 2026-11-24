from database import listar_produtos_agrupados


def buscar_produtos_dos_pedidos(pedidos):
    produtos_por_pedido = {}
    totais_por_pedido = {}

    agrupados = listar_produtos_agrupados() if pedidos else {}

    for pedido in pedidos:
        id_pedido = pedido[0]
        produtos = agrupados.get(id_pedido, [])
        total = 0

        for produto in produtos:
            total = total + produto[2]

        produtos_por_pedido[id_pedido] = produtos
        totais_por_pedido[id_pedido] = total

    return produtos_por_pedido, totais_por_pedido
