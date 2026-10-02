import sqlite3

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


# Insere um novo pedido na tabela
cursor.execute("""
    INSERT INTO pedido (tempo, etapa)
    VALUES (?, ?)
""", (5, "Separação"))

# Confirma e salva a alteração no banco
conexao.commit()


# Define qual pedido queremos alterar, consultar e apagar
id_pedido = 3


# Atualiza a etapa do pedido
cursor.execute("""
    UPDATE pedido
    SET etapa = ?
    WHERE id = ?
""", ("Preparo", id_pedido))

# Salva a alteração feita pelo UPDATE
conexao.commit()


# Busca o pedido pelo ID
cursor.execute("""
    SELECT * FROM pedido
    WHERE id = ?
""", (id_pedido,))

# Pega o primeiro resultado encontrado
pedido = cursor.fetchone()

# Mostra o pedido encontrado
print("Pedido encontrado:", pedido)


# Apaga o pedido pelo ID
cursor.execute("""
    DELETE FROM pedido
    WHERE id = ?
""", (id_pedido,))

# Salva a exclusão no banco
conexao.commit()


# Fecha a conexão com o banco
conexao.close()