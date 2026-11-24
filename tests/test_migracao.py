import os
import sqlite3
import unittest
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory


class MigracaoTest(unittest.TestCase):
    def test_migra_banco_antigo_e_preserva_pedidos_e_expediente(self):
        pasta = TemporaryDirectory()
        self.addCleanup(pasta.cleanup)
        anterior = Path.cwd()
        os.chdir(pasta.name)
        self.addCleanup(os.chdir, anterior)

        with closing(sqlite3.connect("foodpoint.db")) as banco, banco:
            banco.execute("CREATE TABLE pedido (id INTEGER PRIMARY KEY, tempo INTEGER NOT NULL, etapa TEXT NOT NULL)")
            banco.executemany("INSERT INTO pedido VALUES (?, ?, ?)", [
                (1, 0, "Separação"), (2, 5, "Entrega"),
            ])

        import database

        database.criar_tabelas()
        separacao = database.buscar_pedido(1)
        self.assertEqual(separacao[:3], (1, 0, "Separação"))
        self.assertIsInstance(separacao[3], int)
        self.assertEqual(database.buscar_pedido(2), (2, 5, "Entrega", None))
        self.assertTrue(database.consultar_expediente_aberto())

        database.atualizar_expediente(False)
        database.criar_tabelas()
        self.assertFalse(database.consultar_expediente_aberto())
        self.assertEqual(database.buscar_pedido(1), separacao)
