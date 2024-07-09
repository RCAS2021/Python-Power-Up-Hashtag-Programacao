# Python Power Up - Hashtag Programacao
    Python Power Up - Automação de tarefas na Primeira Aula da Jornada Python da Hashtag Programação

# Desafio
    Automatizar cadastro de produtos a partir de arquivo csv em sistema web, para ser executado diariamente e sob demanda.

# Bibliotecas utilizadas
- pyautogui
- pandas
- time

# Arquivos
- main.py: Realiza as automações
- auxiliar.py: Descobre a posição dos campos na tela


# Passos realizados
- Passo 1: Entrar no sistema da empresa através do link
    - Abrir o navegador
        - Apertar tecla windows do computador
        - Digitar Chrome
        - Apertar enter
    - Entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
        - Digitar o link
        - Apertar enter
        - Aguardar o site

- Passo 2: Fazer login
    - Selecionar campo de email
        - Selecionar tudo no campo caso haja auto preenchimento
    - Digitar email
    - Selecionar campo de senha
        - Selecionar tudo no campo caso haja auto preenchimento
    - Digitar senha
    - Clicar no botão logar

- Passo 3: Importar a base de dados
    - Armazenar a base de dados em uma variável utilizando o pandas
    
- Passo 4: Cadastrar produto
    - Selecionar campo código do produto
    - Digitar código do produto
    - Selecionar campo marca
    - Digitar marca do produto
    - Selecionar campo tipo
    - Digitar tipo do produto
    - Selecionar campo categoria
    - Digitar categoria do produto
    - Selecionar campo preço unitario
    - Digitar preço unitário do produto
    - Selecionar campo custo
    - Digitar custo do produto
    - Selecionar campo observações
    - Digitar observações do produto
    - Clicar no botão enviar
    - Scrollar para o topo da página

- Passo 5: Repetir passo 4 até cadastrar todos os produtos
    - Adicionar estrutura de repetição for para passar por cada linha da base de dados, repetindo o passo 4