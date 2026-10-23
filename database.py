
import sqlite3


NOME_BANCO = "foodpoint.db"


def conectar():
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tempo INTEGER NOT NULL DEFAULT 0,
            etapa TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            valor REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedido_produto (
            id_pedido INTEGER NOT NULL,
            id_produto INTEGER NOT NULL,
            FOREIGN KEY (id_pedido) REFERENCES pedido(id),
            FOREIGN KEY (id_produto) REFERENCES produto(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_etapas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pedido INTEGER NOT NULL,
            etapa TEXT NOT NULL,
            tempo INTEGER NOT NULL,
            FOREIGN KEY (id_pedido) REFERENCES pedido(id)
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_produto(produto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produto (item, valor)
        VALUES (?, ?)
    """, (produto.item, produto.valor))

    produto.id = cursor.lastrowid

    conexao.commit()
    conexao.close()


def salvar_pedido(pedido):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO pedido (tempo, etapa)
            VALUES (?, ?)
        """, (0, "Separação"))

        id_pedido = cursor.lastrowid

        for produto in pedido.produtos:
            if produto.id is not None:
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
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, tempo, etapa
        FROM pedido
        WHERE etapa != 'Entrega'
        ORDER BY id DESC
    """)

    pedidos = cursor.fetchall()
    conexao.close()

    return pedidos


def listar_todos_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, tempo, etapa
        FROM pedido
        ORDER BY id DESC
    """)

    pedidos = cursor.fetchall()
    conexao.close()

    return pedidos


def contar_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedido")
    total = cursor.fetchone()[0]

    conexao.close()
    return total


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, item, valor
        FROM produto
        ORDER BY id
    """)

    produtos = cursor.fetchall()
    conexao.close()

    return produtos


def listar_produtos_do_pedido(id_pedido):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT produto.id, produto.item, produto.valor
        FROM produto
        JOIN pedido_produto
            ON produto.id = pedido_produto.id_produto
        WHERE pedido_produto.id_pedido = ?
    """, (id_pedido,))

    produtos = cursor.fetchall()
    conexao.close()

    return produtos


def buscar_pedido(id_pedido):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, tempo, etapa
        FROM pedido
        WHERE id = ?
    """, (id_pedido,))

    pedido = cursor.fetchone()
    conexao.close()

    return pedido


def atualizar_pedido(nova_etapa, id_pedido):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pedido
        SET etapa = ?
        WHERE id = ?
    """, (nova_etapa, id_pedido))

    conexao.commit()
    conexao.close()



def registrar_tempo_etapa(id_pedido, etapa, tempo):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO historico_etapas (id_pedido, etapa, tempo)
            VALUES (?, ?, ?)
        """, (id_pedido, etapa, tempo))

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


def listar_historico_etapas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, id_pedido, etapa, tempo
        FROM historico_etapas
        ORDER BY id
    """)

    historico = cursor.fetchall()
    conexao.close()

    return historico


def listar_historico_pedido(id_pedido):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, id_pedido, etapa, tempo
        FROM historico_etapas
        WHERE id_pedido = ?
        ORDER BY id
    """, (id_pedido,))

    historico = cursor.fetchall()
    conexao.close()

    return historico


def deletar_pedido(id_pedido):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            DELETE FROM historico_etapas
            WHERE id_pedido = ?
        """, (id_pedido,))

        cursor.execute("""
            DELETE FROM pedido_produto
            WHERE id_pedido = ?
        """, (id_pedido,))

        cursor.execute("""
            DELETE FROM pedido
            WHERE id = ?
        """, (id_pedido,))

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


criar_tabelas()
