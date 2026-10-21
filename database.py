
import sqlite3


def conectar():
    conexao = sqlite3.connect("foodpoint.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabelas():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tempo INTEGER,
                etapa TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT,
                valor REAL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedido_produto (
                id_pedido INTEGER,
                id_produto INTEGER,
                FOREIGN KEY (id_pedido) REFERENCES pedido(id),
                FOREIGN KEY (id_produto) REFERENCES produto(id),
                PRIMARY KEY (id_pedido, id_produto)
            )
        """)

        conexao.commit()

    finally:
        conexao.close()


def salvar_produto(produto):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO produto (item, valor)
            VALUES (?, ?)
        """, (produto.item, produto.valor))

        conexao.commit()

        produto.id = cursor.lastrowid
        return produto.id

    finally:
        conexao.close()


def salvar_pedido(pedido):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO pedido (tempo, etapa)
            VALUES (?, ?)
        """, (pedido.tempo, pedido.etapa))

        id_pedido = cursor.lastrowid

        for produto in pedido.produtos:
            if produto.id is None:
                raise ValueError(
                    f"O produto '{produto.item}' precisa ser salvo primeiro."
                )

            cursor.execute("""
                INSERT INTO pedido_produto (id_pedido, id_produto)
                VALUES (?, ?)
            """, (id_pedido, produto.id))

        conexao.commit()
        return id_pedido

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


def listar_pedidos():
    conexao = conectar()

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pedido")
        return cursor.fetchall()

    finally:
        conexao.close()


def listar_produtos():
    conexao = conectar()

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produto")
        return cursor.fetchall()

    finally:
        conexao.close()


def listar_produtos_do_pedido(id_pedido):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT produto.id, produto.item, produto.valor
            FROM produto
            INNER JOIN pedido_produto
                ON produto.id = pedido_produto.id_produto
            WHERE pedido_produto.id_pedido = ?
        """, (id_pedido,))

        return cursor.fetchall()

    finally:
        conexao.close()


def buscar_pedido(id_pedido):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM pedido
            WHERE id = ?
        """, (id_pedido,))

        return cursor.fetchone()

    finally:
        conexao.close()


def atualizar_pedido(nova_etapa, id_pedido):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE pedido
            SET etapa = ?
            WHERE id = ?
        """, (nova_etapa, id_pedido))

        conexao.commit()

    finally:
        conexao.close()


def deletar_pedido(id_pedido):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM pedido_produto
            WHERE id_pedido = ?
        """, (id_pedido,))

        cursor.execute("""
            DELETE FROM pedido
            WHERE id = ?
        """, (id_pedido,))

        conexao.commit()

    finally:
        conexao.close()


criar_tabelas()
