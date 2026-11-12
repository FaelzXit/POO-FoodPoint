
import math
import os
import requests
import time

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

from pedidos.cadastro import criar_pedido
from pedidos.consulta import buscar_produtos_dos_pedidos



app = Flask(__name__)

expediente_aberto = True

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
    produtos_por_pedido, totais_por_pedido = buscar_produtos_dos_pedidos(
        todos_pedidos
    )

    return render_template(
        "pedidos.html",
        pedidos=pedidos,
        todos_pedidos=todos_pedidos,
        total_pedidos=total_pedidos,
        historicos=historicos,
        produtos_por_pedido=produtos_por_pedido,
        totais_por_pedido=totais_por_pedido
    )


@app.route("/cadastrar", methods=["POST"])
def cadastrar_pedido():
    if not expediente_aberto:
        flash("O expediente foi encerrado. Não é possível avançar pedidos.")
        return redirect(url_for("pagina_inicial"))
    pedido, erro = criar_pedido(request.form)

    if erro is not None:
        flash(erro)
        return redirect(url_for("pagina_inicial"))

    try:
        id_pedido = salvar_pedido(pedido)
        total = pedido.somar_produtos()
        flash(f"Pedido #{id_pedido} cadastrado! Total: R$ {total:.2f}.")

    except Exception:
        app.logger.exception("Erro ao cadastrar pedido.")
        flash("Não foi possível cadastrar o pedido. Confira o terminal.")

    return redirect(url_for("pagina_inicial"))


@app.route("/avancar_pedido/<int:id_pedido>", methods=["POST"])
def avancar_pedido(id_pedido):
    if not expediente_aberto:
        flash("O expediente foi encerrado. Não é possível cadastrar pedidos.")
        return redirect(url_for("pagina_inicial"))
    pedido = buscar_pedido(id_pedido)

    if pedido is None:
        flash("Pedido não encontrado.")
        return redirect(url_for("pagina_inicial"))

    etapa_atual = pedido[2]

    try:
        if etapa_atual == "Separação":
            inicio_separacao = pedido[3]
            if inicio_separacao is None:
                inicio_separacao = int(time.time())

            segundos_separacao = max(
                0,
                int(time.time()) - int(inicio_separacao)
            )
            minutos_separacao = max(1, math.ceil(segundos_separacao / 60))

            registrar_tempo_etapa(
                id_pedido,
                "Separação",
                minutos_separacao
            )
            atualizar_pedido("Preparo", id_pedido)
            flash(
                f"Pedido #{id_pedido} iniciou Preparo. "
                f"Tempo de Separação: {minutos_separacao} min."
            )

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

@app.route("/finalizar-expediente", methods=["POST"])
def finalizar_expediente():
    global expediente_aberto
    expediente_aberto = False

    todos_pedidos = listar_todos_pedidos()
    historicos = {}

    for pedido in todos_pedidos:
        id_pedido = pedido[0]
        historicos[id_pedido] = listar_historico_pedido(id_pedido)

    dados_expediente = {
        "total_pedidos": len(todos_pedidos),
        "historicos": historicos,
    }

    try:
        resposta = requests.post(
            "http://127.0.0.1:5001/api/expediente",
            json=dados_expediente,
            timeout=120,
        )
        resposta.raise_for_status()
        flash("Expediente finalizado. Dados enviados ao FoodPoint.")
    except requests.RequestException:
        app.logger.exception("Não foi possível enviar os dados ao FoodPoint.")
        flash("Expediente finalizado, mas não foi possível enviar os dados ao FoodPoint.")

    return redirect(url_for("pagina_inicial"))
if __name__ == "__main__":
    app.run(debug=True)
