import pyautogui
import pandas as pd
import openpyxl
import numpy
import time

# Passo 1: Entrar no sistema da empresa através do link
# Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Preencher login
# Passo 3: Preencher senha
# Passo 4: Clicar em logar
# Passo 5: Importar a base de dados
# Passo 6: Preencher dados
# Passo 7: Clicar em cadastrar
# Passo 8: Repetir passo 6 até cadastrar todos os produtos

# Link do sistema
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Adicionando pausa entre os comandos para evitar erros
pyautogui.PAUSE = 1

# Passo 1:
# Abrir o navegador
# Apertar tecla windows do computador
pyautogui.press('win')

# Digitar chrome
pyautogui.write('chrome')

# Apertar enter
pyautogui.press('enter')

# Entrar no link
# Digitar o link
pyautogui.write(link)

# Apertar enter
pyautogui.press('enter')

# Aguardar o site carregar
time.sleep(3)

# Passo 2:
# Posições dos campos e botões
# Posição do campo email
pos_email = [1396, 471]

# Posição do campo senha
pos_senha = [1396, 604]

# Posição do botão logar
pos_logar = [1270, 674]

# Fazer login
# Selecionar campo de email
pyautogui.click(x=pos_email[0], y=pos_email[1])

# Prevenindo auto preenchimento
# Selecionar tudo no campo -> ctrl + a
pyautogui.hotkey('ctrl', 'a')

# Digitar o email
pyautogui.write('email@email.com')

# Selecionar campo de senha
pyautogui.click(x=pos_senha[0], y=pos_senha[1])

# Selecionando tudo para evitar auto preenchimento
pyautogui.hotkey('ctrl', 'a')

# Digitar a senha
pyautogui.write('Senha@123')

# Clicar no botão logar
pyautogui.click(x=pos_logar[0], y=pos_logar[1])

# Aguardar a página carregar
time.sleep(3)

# Passo 3:
# Importar a base de dados
produtos = pd.read_csv('produtos.csv')

# Passo 4 e 5:
# Percorrendo as linhas da tabela
for r in produtos.index:
    # Cadastrar produto
    # Posição do campo de código do produto
    pos_cod = [1343, 320]

    # Código
    # Selecionar o campo código do produto
    pyautogui.click(x=pos_cod[0], y=pos_cod[1])

    # Digitar código
    pyautogui.write(produtos.codigo[r])
    # Selecionar próximo campo
    pyautogui.press('tab')

    # Marca
    pyautogui.write(produtos.marca[r])
    pyautogui.press('tab')

    # Tipo
    pyautogui.write(produtos.tipo[r])
    pyautogui.press('tab')

    # Categoria
    pyautogui.write(str(produtos.categoria[r]))
    pyautogui.press('tab')

    # Preço Unitário
    pyautogui.write(str(produtos.preco_unitario[r]))
    pyautogui.press('tab')

    # Custo
    pyautogui.write(str(produtos.custo[r]))
    pyautogui.press('tab')

    # Observações
    pyautogui.write(str(produtos.obs[r]))
    pyautogui.press('tab')

    # Clicar no botão de enviar
    pyautogui.press('enter')

    # Voltar ao topo utilizando home
    pyautogui.press('home')

    # Outra opção -> voltar ao topo utilizando scroll
    # pyautogui.scroll(-1000)
  