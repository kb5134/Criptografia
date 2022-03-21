#encoding:utf-8
from re import A
import re
import config #configurar as info do banco
import pyqrcode #pip3 install pyqrcode e pip3 install  pypng
from random import randint
import sys

key = ''
'''funcao para criptografar o texto.'''
def encrypt():

    texto = input('insira a mensagem: ').upper()

    if len(texto) <= 200: #verifica quantidade maxima de letras no texto
        dicionario = {  #gera um dicionario com numeros aleatorios de 1 a 99 para cada letra do alfabeto
            "A": randint(1,99),
            "B": randint(1,99),
            "C": randint(1,99),
            "D": randint(1,99),
            "E": randint(1,99),
            "F": randint(1,99),
            "G": randint(1,99),
            "H": randint(1,99),
            "I": randint(1,99),
            "J": randint(1,99),
            "K": randint(1,99),
            "L": randint(1,99),
            "M": randint(1,99),
            "N": randint(1,99),
            "O": randint(1,99),
            "P": randint(1,99),
            "Q": randint(1,99),
            "R": randint(1,99),
            "S": randint(1,99),
            "T": randint(1,99),
            "U": randint(1,99),
            "V": randint(1,99),
            "W": randint(1,99),
            "X": randint(1,99),
            "Y": randint(1,99),
            "Z": randint(1,99)
        }
        for letras in texto: #Para cada letra no texto, transforma a letra no valor aleatori gerado no dicionario
            letras = dicionario[letras]
            print(letras, end=' ')
            
       #Salva o dicionario e a chave de aceesso no banco de dados
        mycursor = config.mydb.cursor()
        sql = "INSERT INTO gulosa (chave, dicionarios) VALUES (%s, %s)"
        val = (f"{key}", f"{str(dicionario)}") #define os valores a serem inseridos no banco
        mycursor.execute(sql, val)
        config.mydb.commit()


    else: #se a mensagem for maior que o limeite, exibe um erro e para a execução
        sys.exit("Limite atingido")
        
#função que gera a senha de acesso que será inserida no qrcode
def senha():
    global key
    key = str(randint(1,50))

# função que gera o qrcode e salva a chave no mesmo
def qrcode():
    qrkey= pyqrcode.create(key)
    print( '\n', 'escaneie o qr code para ter acesso a chave de acesso para o dicionario')
    qrkey.show()

'''Descriptografa a mensagem'''
def decrypt():
    recebekey = int(input('digite a chave de acesso: ')) #solicita a chave de acesso ao dicionario
    
    #le as informações do banco
    mycursor = config.mydb.cursor()
    select_chave = f"SELECT chave FROM gulosa where chave={recebekey}" #pega a chave salva no banco
    mycursor.execute(select_chave)
    retorno = mycursor.fetchone()
    chave = int(str(retorno).replace(',','').replace('(','').replace(')', '')) #trata a varivel para que a mesma seja usada posteriormente


    if recebekey == chave: #verifica se a chave inserda é igual a chave que existe no banco

        recebetexto = input('digite o texto criptografado: ').replace(" ",',').split(',') #solicita texto e trata o mesmo
        
        # pega o dicionario salvo no banco para a chave inserida
        select_dicionario = f"SELECT dicionarios FROM gulosa where chave={recebekey}"
        mycursor.execute(select_dicionario)
        retorno = mycursor.fetchone()

        #converte o retorno de tupla para string e de string para dicionario        
        converte_dicionario = ''.join(retorno)
        converte_dicionario = dict(subString.split(":") for subString in converte_dicionario.split(",")) 

        valores = [] 
        for chave in converte_dicionario.keys():
            valores.append(converte_dicionario[chave].strip(" ")) #para cada chave no dicionario, adiciona a mesma em uma lista
        dicionario_final = {  #Cria um dicionario utilizando as chaves da lista como chaves e definindo os valores do banco para o alfabeto
            valores[0]:  "A",
            valores[1]:  "B",
            valores[2]:  "C",
            valores[3]:  "D",
            valores[4]:  "E",
            valores[5]:  "F",
            valores[6]:  "G",
            valores[7]:  "H",
            valores[8]:  "I",
            valores[9]: "J",
            valores[10]: "K",
            valores[11]: "L",
            valores[12]: "M",
            valores[13]: "N",
            valores[14]: "O",
            valores[15]: "P",
            valores[16]: "Q",
            valores[17]: "R",
            valores[18]: "S",
            valores[19]: "T",
            valores[20]: "U",
            valores[21]: "V",
            valores[22]: "W",
            valores[23]: "X",
            valores[24]: "Y",
            valores[25]: "Z",
        }
        
        for letra in recebetexto: #para cada letra no texto inserido verifica se o texto está no dicionario
            recebetexto = letra
            if recebetexto in dicionario_final:
                print(dicionario_final[recebetexto], end ='',) #se o texto estiver no dicionario, exibe o valor salvo no dicionario na posição recebida no texto 
        print('\n')

    else:  
        print('a chave de segurança não é valida')
