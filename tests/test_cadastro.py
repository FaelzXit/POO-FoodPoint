import unittest
from decimal import Decimal

from pedidos.cadastro import criar_pedido


class CadastroTest(unittest.TestCase):
    def test_aceita_tres_itens_e_separadores_decimais(self):
        pedido, erro = criar_pedido({
            "item_1": " Lanche ", "valor_1": "10,50",
            "item_2": "Suco", "valor_2": "2.25",
            "item_3": "Fruta", "valor_3": "1",
        })
        self.assertIsNone(erro)
        self.assertEqual(pedido.etapa, "Separação")
        self.assertEqual([p.item for p in pedido.produtos], ["Lanche", "Suco", "Fruta"])
        self.assertEqual(pedido.somar_produtos(), Decimal("13.75"))

    def test_soma_centavos_sem_imprecisao(self):
        pedido, erro = criar_pedido({
            "item_1": "A", "valor_1": "0,10",
            "item_2": "B", "valor_2": "0,20",
        })
        self.assertIsNone(erro)
        self.assertEqual(pedido.somar_produtos(), Decimal("0.30"))

    def test_rejeita_dados_invalidos(self):
        casos = [
            ({}, "Adicione pelo menos"),
            ({"item_1": "Lanche"}, "Preencha"),
            ({"valor_1": "3"}, "Preencha"),
            ({"item_1": "Lanche", "valor_1": "abc"}, "valor válido"),
            ({"item_1": "Lanche", "valor_1": "NaN"}, "entre"),
            ({"item_1": "Lanche", "valor_1": "0"}, "entre"),
            ({"item_1": "Lanche", "valor_1": "100000"}, "entre"),
            ({"item_1": "Lanche", "valor_1": "1,001"}, "duas casas"),
            ({"item_1": "a" * 81, "valor_1": "1"}, "80 caracteres"),
        ]
        for dados, mensagem in casos:
            with self.subTest(dados=dados):
                pedido, erro = criar_pedido(dados)
                self.assertIsNone(pedido)
                self.assertIn(mensagem, erro)
