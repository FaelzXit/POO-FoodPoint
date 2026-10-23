
import os

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    flash
)

from database import (
    salvar_pedido,
    listar_pedidos,
    listar_todos_pedidos,
    contar_pedidos,
    buscar_pedido,
    atualizar_pedido,
    registrar_tempo_etapa,
    listar_historico_pedido
)

from models.pedido import Pedido


app = Flask(__name__)

app.secret_key = os.environ.get(
    "FLASK_SECRET_KEY",
    "chave-apenas-para-desenvolvimento"
)


@app.route("/")
def pagina_inicial():
    pedidos = listar_pedidos()
    todos_pedidos = listar_todos_pedidos()
    total_pedidos = contar_pedidos()

    historicos = {
        pedido[0]: listar_historico_pedido(pedido[0])
        for pedido in todos_pedidos
    }

    return render_template(
        "pedidos.html",
        pedidos=pedidos,
        todos_pedidos=todos_pedidos,
        total_pedidos=total_pedidos,
        historicos=historicos
    )


@app.route("/cadastrar", methods=["POST"])
def cadastrar_pedido():
    pedido = Pedido(0, "Separação", [])

    try:
        id_pedido = salvar_pedido(pedido)
        flash(f"Pedido #{id_pedido} cadastrado com sucesso!")

    except Exception:
        app.logger.exception("Erro ao cadastrar pedido.")
        flash("Não foi possível cadastrar o pedido. Confira o terminal.")

    return redirect(url_for("pagina_inicial"))


@app.route("/avancar_pedido/<int:id_pedido>", methods=["POST"])
def avancar_pedido(id_pedido):
    pedido = buscar_pedido(id_pedido)

    if pedido is None:
        flash("Pedido não encontrado.")
        return redirect(url_for("pagina_inicial"))

    etapa_atual = pedido[2]

    try:
        if etapa_atual == "Separação":
            atualizar_pedido("Preparo", id_pedido)
            flash(f"Pedido #{id_pedido} avançou para Preparo.")

        elif etapa_atual == "Preparo":
            tempo = request.form.get("tempo", type=int)

            if tempo is None or tempo <= 0:
                flash("Informe um tempo de preparo maior que zero.")
                return redirect(url_for("pagina_inicial"))

            registrar_tempo_etapa(
                id_pedido,
                "Preparo",
                tempo
            )

            atualizar_pedido("Finalização", id_pedido)

            flash(
                f"Tempo de Preparo registrado para o pedido #{id_pedido}."
            )

        elif etapa_atual == "Finalização":
            tempo = request.form.get("tempo", type=int)

            if tempo is None or tempo <= 0:
                flash("Informe um tempo de finalização maior que zero.")
                return redirect(url_for("pagina_inicial"))

            registrar_tempo_etapa(
                id_pedido,
                "Finalização",
                tempo
            )

            atualizar_pedido("Entrega", id_pedido)

            flash(
                f"Pedido #{id_pedido} entregue e finalizado com sucesso!"
            )

        elif etapa_atual == "Entrega":
            flash("Esse pedido já foi finalizado.")

        else:
            flash("A etapa atual do pedido é inválida.")

    except Exception:
        app.logger.exception("Erro ao avançar pedido.")
        flash("Não foi possível atualizar o pedido. Confira o terminal.")

    return redirect(url_for("pagina_inicial"))


if __name__ == "__main__":
    app.run(debug=True)
