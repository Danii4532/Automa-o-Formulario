import time
import tkinter

import selenium
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd
total_planilhas = []

dicionario = {}

def Validar_xpath(xpath_fornecido):
    #validar cada xpath fornecido pelo usuario
    from lxml import html
    import requests

    # URL da página da web
    url = link

    # XPath fornecido
    xpath = xpath_fornecido

    # Faz uma requisição HTTP para obter o conteúdo da página da web
    resposta = requests.get(url)

    # Analisa o conteúdo HTML da página usando LXML
    arvore = html.fromstring(resposta.content)

    # Encontra o elemento correspondente ao XPath na página
    elementos = arvore.xpath(xpath)

    # Verifica se o elemento foi encontrado
    if elementos:
        return True
    else:
        return False


def Analisar_link():
    #analisa se o link gerado pelo usuario esta online ou é valido ou não
    try:
        # Faz uma requisição HTTP ao link
        resposta = requests.get(link)

        # Verifica o código de status da resposta
        if resposta.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        # Se ocorrer um erro na requisição (por exemplo, o host não pôde ser resolvido)
        return False

def Abrir_arquivo():
    #funcao para verificar que tipo de arquivo será usado para preencher cada campo do formulario, funcao deve retornar uma lista com os valores escolhidos prontos
    valores_planilhas = []
    op = input(f'Para prencher o {lista_chave[contador]} será usado:  \n1 - Planilha  \n2 - Texto  \n3 - Lista  \n4 - Valor fixo  \n:')

    if op == '3':
        print(f'Serão inseridas {numero_informacoes} informações')
        lista_informacoes = []
        for item in range(numero_informacoes):
            valor = input(f'Digite o {item+1} valor: ')
            lista_informacoes.append(valor)
        return lista_informacoes

    elif op == '4':
        lista_valor_fixo = []
        valor_fixo = input('Insira o valor fixo: ')
        for v in range(numero_informacoes): lista_valor_fixo.append(valor_fixo)
        return lista_valor_fixo

    elif op in ['1','2']:
        #selecionando arquivo
        janela = tkinter.Tk()
        caminho = filedialog.askopenfilename()
        janela.destroy()
        if not caminho:
            print('Nenhum Arquivo Selecionado')
            exit()
        if op == '1':
            if caminho.endswith('xlsx'):
                planilha = pd.read_excel(caminho)
                for coluna in planilha:
                    if str(coluna).startswith('Unnamed'):
                        planilha = planilha.drop(columns=coluna)

                nome_coluna = input('Digite o nome da coluna: ')
                if nome_coluna in planilha:
                    if planilha[nome_coluna].dtypes == 'datetime64[ns]':
                        planilha[nome_coluna] = pd.to_datetime(planilha[nome_coluna])
                        planilha[nome_coluna] = planilha[nome_coluna].dt.strftime('%d/%m/%Y')

                    for i, celula in enumerate(planilha[nome_coluna]):
                        if celula == '' or pd.isna(celula):
                            planilha.loc[i,nome_coluna] = 'Nulo'
                    if planilha[nome_coluna].count() != numero_informacoes:
                        print(f'A coluna da planilha precisa ter {numero_informacoes} valores, porem tem {len(planilha[nome_coluna])} \nPrograma Encerrado')
                        exit()
                    return list(planilha[nome_coluna])
                else:
                    print('Coluna não esta na planilha')

        elif op == '2':
            if caminho.endswith('.txt'):
                with open(caminho,'r') as arquivo:
                    texto = []
                    quantidade_linhas = arquivo.readlines()
                    for linha in quantidade_linhas:
                        if linha.strip() != '':
                            texto.append(linha.strip())
                        elif linha.strip() == '':
                            pass
                    #contando a quantidade de linhas que o txt possui
                    if len(texto) != numero_informacoes:
                        print(f'O arquivo de texto deve conter {numero_informacoes} linhas, mas contem {len(texto)}')
                    return texto
        else:
            print('Opção inválida')
            print('Programa encerrado')
            exit()
    else:
        print('Opção Inválida')
        print('Programa Encerrado')
        exit()



link = input('Digite o link do formulario: ')
confirmacao = Analisar_link()
if confirmacao:
    pass
else:
    print('O link fornecido não esta disponivel')
    exit()

#solicitando continuade de campos e quantidade de dados que serao usados
numero_planilhas = input('Quantas campos serão preenchidos: ')
if numero_planilhas.isdigit() == False:
    print('Insira apenas numeros')
    exit()
else:
    numero_planilhas = int(numero_planilhas)
if numero_planilhas > 10:
    print('Não é possível inserir mais de 10 campos')
    exit()
numero_informacoes = int(input('Digite quantos dados cada planilha possui: '))



for cada in range(numero_planilhas):
    chave = input('Digite o nome do campo: ')
    valor = input(f'Digite o xpath do campo {chave}: ')
    novo_valor = Validar_xpath(valor)
    if novo_valor:
        dicionario[chave] = str(valor)
    else:
        print('O xpath fornecido é invalido')
        exit()

botao = input('Digite o xpath do botão: ')
novo_valor = Validar_xpath(botao)
if novo_valor:
    dicionario['botao'] = str(botao)
else:
    print('O xpath fornecido é invalido')
    exit()


contador = 0


#ativando webdrive e entrando no site
lista_chave = list(dicionario.keys())
lista_valores = list(dicionario.values())

for cada_lista in range(numero_planilhas):
    lista = Abrir_arquivo()
    total_planilhas.append(lista)
    contador+=1

navegador = webdriver.Chrome()
navegador.get(link)
m = 0

for t in range(numero_informacoes):
    for r in range(numero_planilhas):
        print(f'{t+1} - {lista_chave[r]}  : {total_planilhas[r][t]}')
        time.sleep(0.2)
        info = navegador.find_element(By.XPATH, lista_valores[r])
        if info.is_displayed():
            #print("O elemento está visível na página.")
            pass
        else:
            print("O elemento não está visível na página.")

        # Verifica se o elemento está habilitado para interação
        if info.is_enabled():
            #print("O elemento está habilitado para interação.")
            pass
        else:
            print("O elemento não está habilitado para interação.")
        info.send_keys(total_planilhas[r][t])
        if r == (numero_planilhas-1):
            p = navegador.find_element(By.XPATH,dicionario['botao'])
            p.click()
            print('\n')
    

navegador.quit()
