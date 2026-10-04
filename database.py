import sqlite3

from models.pedido import Pedido

# Cria uma conexão com o banco de dados
conexao = sqlite3.connect("foodpoint.db")

# Cria o cursor, que será usado para executar os comandos SQL
cursor = conexao.cursor()

# Cria a tabela "pedido" caso ela ainda não exista
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


def salvar_pedido(pedido):

    cursor.execute("""
        INSERT INTO pedido (tempo, etapa)
        VALUES (?, ?)
    """, (pedido.tempo, pedido.etapa))

    conexao.commit()
    
    return cursor.lastrowid 

def salvar_produto(produto):
    cursor.execute("""
                   
                   INSERT INTO produto (item, valor)
                   VALUES(?,?)
                   
                   """, (produto.item, produto.valor))
    conexao.commit

def listar_pedidos():

    cursor.execute("""
        SELECT * FROM pedido
    """)

    pedidos = cursor.fetchall()

    return pedidos

def listar_produtos():
    cursor.execute("""
                   
                   SELECT * FROM produto
                   
                   """)
    produtos = cursor.fetchall()
    
    return produtos

def buscar_pedido(id_pedido):
    
    cursor.execute("""
                   
                   SELECT * FROM pedido
                   WHERE id = ?
                   
                   """,(id_pedido,))
    pedido = cursor.fetchone()
    return pedido
    
def atualizar_pedido(nova_etapa, id_pedido):

    cursor.execute("""
        UPDATE pedido
        SET etapa = ?
        WHERE id = ?
    """, (nova_etapa, id_pedido))
    
    conexao.commit()
    

def deletar_pedido(id_pedido):

    cursor.execute("""
        DELETE FROM pedido
        WHERE id = ?
    """, (id_pedido,))
