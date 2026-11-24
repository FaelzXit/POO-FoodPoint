# Cadastro simples de pedidos

Este diretório guarda a parte de registrar produtos e seus valores no FoodPoint.
O formulário envia os dados para o Python, que cria os objetos `Produto` e `Pedido`
e salva tudo usando o banco SQLite do projeto.

O cadastro foi feito com um formulário HTML e comandos básicos de Python. Cada
linha representa uma unidade do produto, e o formulário aceita até três linhas.

O fluxo de etapas e o registro dos tempos ficam em `app.py`, que também
permite encerrar e reabrir o expediente. O estado do expediente fica no SQLite.

## Arquivos relacionados

- `pedidos/cadastro.py`: valida e monta o pedido.
- `pedidos/consulta.py`: consulta os produtos e calcula os totais.
- `templates/pedidos.html`: formulário e painel de pedidos.
- `static/timer-separacao.js`: cronômetro da etapa de Separação.
