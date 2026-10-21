
from flask import Flask, render_template, request, redirect, url_for
from database import (
    listar_pedidos,
    salvar_pedido,
    atualizar_pedido,
    deletar_pedido
)
from models.pedido import Pedido

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    pedidos = listar_pedidos()
    return render_template("pedidos.html", pedidos=pedidos)


@app.route("/cadastrar", methods=["POST"])
def cadastrar_pedido():
    tempo = int(request.form["tempo"])
    etapa = request.form["etapa"]

    pedido = Pedido(tempo, etapa, [])
    salvar_pedido(pedido)

    return redirect(url_for("pagina_inicial"))


@app.route("/alterar_etapa/<int:id_pedido>", methods=["POST"])
def alterar_etapa(id_pedido):
    nova_etapa = request.form["etapa"]

    atualizar_pedido(nova_etapa, id_pedido)

    return redirect(url_for("pagina_inicial"))


@app.route("/deletar/<int:id_pedido>", methods=["POST"])
def excluir_pedido(id_pedido):
    deletar_pedido(id_pedido)

    return redirect(url_for("pagina_inicial"))


if __name__ == "__main__":
    app.run(debug=True)
