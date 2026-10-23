# FoodPoint — aprendizado de Python na prática

Este repositório acompanha meu aprendizado de **Programação Orientada a Objetos com Python**. A proposta é desenvolver o FoodPoint etapa a etapa, aplicando no projeto os conceitos estudados em vez de deixar o conteúdo apenas na teoria.

A cada nova etapa, o sistema ganha uma pequena parte e o código serve como registro prático do que estou aprendendo: modelar objetos, organizar arquivos, conversar com um banco de dados e construir uma aplicação web.

## Sobre o projeto

O FoodPoint é um sistema simples para acompanhar pedidos de uma cozinha. No momento, é possível cadastrar pedidos, avançá-los pelas etapas de produção e registrar os tempos de preparo e finalização.

O projeto está em desenvolvimento e representa o conhecimento aplicado até aqui. O **HTML e o CSS** foram criados com o **Antigravity** para auxiliar no design da aplicação e trazer ideias inovadoras para a interface. O backend e a lógica em **Python** foram desenvolvidos com apoio do ChatGPT durante o processo de aprendizado.

## O que estou praticando

### Python e orientação a objetos

- Criar classes e instanciar objetos;
- Definir atributos, métodos e construtores (`__init__`);
- Usar `self` para acessar dados do objeto;
- Representar pedidos e produtos por meio das classes `Pedido` e `Produto`;
- Organizar o código em módulos e pastas;
- Trabalhar com listas de objetos e valores retornados por funções.

### Banco de dados

- Usar SQLite para guardar informações entre execuções;
- Criar tabelas e relacioná-las por chaves;
- Executar operações de consulta e alteração de dados;
- Aplicar operações CRUD (criar, ler, atualizar e excluir);
- Registrar o histórico dos tempos de cada etapa do pedido.

### Aplicação web

- Criar rotas com Flask;
- Receber dados de formulários;
- Exibir informações do Python em templates HTML com Jinja;
- Separar a estrutura HTML dos estilos CSS;
- Atualizar o status dos pedidos conforme as ações do usuário.

## Evolução do projeto

O desenvolvimento acontece gradualmente. Até agora, o projeto passou por estas etapas:

1. **Modelagem inicial:** criação das classes `Pedido` e `Produto` para representar os dados do domínio.
2. **Persistência:** configuração do SQLite e criação das tabelas para pedidos, produtos e relações entre eles.
3. **Operações com dados:** implementação de funções para cadastrar, consultar, atualizar e excluir registros.
4. **Fluxo de pedidos:** definição das etapas Separação, Preparo, Finalização e Entrega.
5. **Histórico de tempos:** registro dos minutos informados para Preparo e Finalização.
6. **Interface web:** conexão do backend Flask com uma página HTML e seus estilos CSS.

Essa lista registra o caminho percorrido até o momento; novas funcionalidades e conceitos serão adicionados conforme os estudos avançarem.

## Estrutura atual

```text
POO-FoodPoint/
├── app.py                 # Rotas Flask e fluxo principal da aplicação
├── database.py            # Tabelas e operações com o banco SQLite
├── analise.py             # Exercício de cálculo da mediana de tempos
├── teste_historico.py     # Script auxiliar para experimentar o histórico
├── foodpoint.db           # Banco SQLite
├── models/
│   ├── pedido.py          # Classe Pedido
│   └── produto.py         # Classe Produto
├── templates/
│   └── pedidos.html       # Interface HTML com templates Jinja
└── static/
    └── style.css          # Estilos da interface
```

## Executar o projeto

É necessário ter o **Python 3** instalado. No terminal, dentro da pasta do projeto, instale o Flask:

```bash
python -m pip install Flask
```

Depois, inicie a aplicação:

```bash
python app.py
```

Abra no navegador o endereço indicado pelo Flask, geralmente <http://127.0.0.1:5000>.

O módulo `database.py` cria as tabelas necessárias quando é carregado. Os dados ficam no arquivo `foodpoint.db`.

## Experimentar o fluxo

1. Use **Novo Pedido** para criar um pedido na etapa Separação.
2. Avance o pedido para Preparo.
3. Informe o tempo de preparo em minutos para avançar à Finalização.
4. Informe o tempo de finalização para concluir a entrega.
5. Consulte os tempos no histórico do pedido e no registro geral.

## Próximas etapas

O projeto continua aberto para novos exercícios e melhorias. A função de mediana em `analise.py`, por exemplo, é um estudo inicial de análise de tempos e ainda não está conectada à interface. A ideia é seguir evoluindo o sistema conforme novos assuntos forem aprendidos e aplicados.

> Aplicação desenvolvida para fins de estudo. O modo de depuração do Flask está habilitado para execução local durante o desenvolvimento.

