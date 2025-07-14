# Guia de passos para o projeto:

# 1: Entrar no navegador
# Abrir tecla "Win"
# Pesquisar "Chrome" e dar "Enter"

# 2: Entra no site/sistema da empresa - "file:///C:/Users/L%C3%A9o/Desktop/Projeto%20Automa%C3%A7%C3%A3o/login.html"

# 3: Importar a base de dados

# 4: Cadastrar 1 produto    

# 5: Repetir para todos os produtos


# Utilizarei o PyautoGui para fazer automações com o Python

#OBS: Atenção nessa parte, caso você queira rodar esse sistema na sua máquina, é importante ressaltar que a precisão dos cliques vai variar por conta das telas 
# (monitores e resolução)

#Na parte de rascunho, eu usei o comando print(pyautogui.position()) para achar a posição que o mouse fosse clicar, com essa posição informada, utilizarei
# o pyautogui.click(x=1056, y=568) com as posições preenchidas.


import pyautogui
import time

pyautogui.PAUSE = 0.5

#Abrir o Navegador
pyautogui.press("Win")
time.sleep(1)
pyautogui.write("Chrome")
pyautogui.press("Enter")
time.sleep(1)
pyautogui.click(x=1056, y=568)   #Posição do clique do Mouse
time.sleep(1)

#Entrar no Sistema
pyautogui.write("file:///C:/Users/L%C3%A9o/Desktop/Projeto%20Automa%C3%A7%C3%A3o/login.html")   #Aqui será o diretório da página HTML Local
time.sleep(1)
pyautogui.press("Enter")
time.sleep(1)
pyautogui.click(x=175, y=241)
time.sleep(2)

#Fazer Login na Empresa
pyautogui.write("leonardo@ufsc.com")
pyautogui.press("Tab")
time.sleep(2)
pyautogui.write("123456789")
time.sleep(1)
pyautogui.click(x=71, y=376)   #Posição do Clique do Mouse
time.sleep(1)

#Importar base de Dados
import pandas

planilhas = pandas.read_csv("planilhas_produtos.csv")
print(planilhas)

#Cadastrar 1 produto
#Passar para próximo campo com "Tab"

for linha in planilhas.index:  #Fazer um laço de repetição para acessar a planilha (Index)

    pyautogui.click(x=209, y=196)
    codigo = planilhas.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("Tab")

    marca = planilhas.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("Tab")

    tipo = planilhas.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("Tab")

    categoria = str (planilhas.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("Tab")

    preco_unitario = str (planilhas.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("Tab")

    custo = str (planilhas.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("Tab")
    
    obs = str (planilhas.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.click(x=77, y=734)

    time.sleep(0.5)
    pyautogui.press("Home")

