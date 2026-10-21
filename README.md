# 🍔 FoodPoint

Sistema de gerenciamento e análise da produção de pedidos, desenvolvido em Python com Programação Orientada a Objetos (POO).

## 🎯 Objetivo

Gerenciar pedidos e acompanhar etapas de produção, com a proposta futura de utilizar Inteligência Artificial para identificar gargalos e sugerir melhorias.

## 🛠️ Tecnologias

- Python e POO
- Flask
- SQLite e SQL
- HTML e CSS
- Git e GitHub

## 📂 Estrutura do projeto

```text
POO-FoodPoint/
├── app.py
├── database.py
├── teste_banco.py
├── foodpoint.db
├── models/
│   ├── pedido.py
│   └── produto.py
├── templates/
│   └── pedidos.html
└── static/
    └── style.css
```

## ✅ Funcionalidades implementadas

- Cadastro e consulta de pedidos.
- Atualização da etapa de produção, mantendo o mesmo ID.
- Exclusão de pedidos.
- Cadastro e consulta de produtos no banco.
- Relacionamento entre pedidos e produtos.
- Interface web com Flask, HTML e CSS.

## ▶️ Como executar

Instale o Flask:

```bash
py -m pip install flask
```

Execute a aplicação:

```bash
py app.py
```

Acesse no navegador: `http://127.0.0.1:5000`

## 🚀 Próximos passos

- Validar e melhorar os testes do CRUD.
- Associar produtos aos pedidos pela interface.
- Registrar tempos das etapas de produção.
- Criar indicadores de desempenho.
- Integrar Inteligência Artificial para analisar gargalos.

## 👨‍💻 Sobre

Projeto acadêmico desenvolvido para aplicar POO em Python, banco de dados, desenvolvimento web e integração futura com Inteligência Artificial.
