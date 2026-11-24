import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


class FluxoTest(unittest.TestCase):
    def setUp(self):
        pasta = TemporaryDirectory()
        self.addCleanup(pasta.cleanup)
        anterior = Path.cwd()
        os.chdir(pasta.name)
        self.addCleanup(os.chdir, anterior)

        import app
        import database

        database.criar_tabelas()
        self.database = database
        self.cliente = app.app.test_client()

    def post(self, rota, dados=None):
        resposta = self.cliente.post(rota, data=dados, follow_redirects=True)
        self.assertEqual(resposta.status_code, 200)
        return resposta.get_data(as_text=True)

    def test_avanca_todas_as_etapas_e_registra_os_tempos(self):
        self.post("/cadastrar", {"item_1": "Lanche", "valor_1": "5,25"})
        pedido = self.database.buscar_pedido(1)
        self.assertEqual(pedido[2], "Separação")
        self.post("/avancar_pedido/1")
        self.assertEqual(self.database.buscar_pedido(1)[2], "Preparo")

        self.assertIn("maior que zero", self.post("/avancar_pedido/1", {"tempo": "0"}))
        self.assertEqual(self.database.buscar_pedido(1)[2], "Preparo")
        self.post("/avancar_pedido/1", {"tempo": "3"})
        self.assertEqual(self.database.buscar_pedido(1)[2], "Finalização")

        self.assertIn("maior que zero", self.post("/avancar_pedido/1", {"tempo": "-1"}))
        self.assertEqual(self.database.buscar_pedido(1)[2], "Finalização")
        self.post("/avancar_pedido/1", {"tempo": "4"})
        self.assertEqual(self.database.buscar_pedido(1)[2], "Entrega")
        self.assertIn("já foi finalizado", self.post("/avancar_pedido/1"))
        historico = self.database.listar_historico_pedido(1)
        self.assertEqual([linha[2] for linha in historico], ["Separação", "Preparo", "Finalização"])
        self.assertGreaterEqual(historico[0][3], 1)
        self.assertEqual([linha[3] for linha in historico[1:]], [3, 4])
