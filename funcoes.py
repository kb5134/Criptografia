#encoding:utf-8
import pyqrcode #pip3 install pyqrcode
from random import randint
key = ''
'''funcao para encriptar o texto.'''
def encrypt():
    frase = open('C:/Users/kb/Desktop/python/APS/texto.txt', 'w') #abre um arquivo de texto
    texto = input('insira a mensagem: ')
    frase.write(texto)#salva o texto inserido no arquivo
    frase.close
    print('o texto criptografado é: ', end='')
    codigo = open('C:/Users/kb/Desktop/python/APS/codigo.txt', 'w')#INICIA O TEXTO QUE VAI SALVAR O TEXTO CRIPTOGRAFADO
    codigo.write('')
    for letras in texto: #PARA CADA LETRA NO TEXTO ELE GERA UM NUMERO ALEATORIO
        
        separado = letras
        separado = randint(1,99)
        print(separado, end=' ')
        codigo.write(str(separado)+ ' ')
    codigo.close()
'''FUNCAO QUE SALVA A SENHA DE ACRESO NA VARIAVEL GLOBAL KEY'''
def senha():
    global key
    key = str(randint(1,10))
'''FUNÇÃO QUE GERA O QR CODE'''
def qrcode():
    qrkey= pyqrcode.create(key)
    print( '\n', 'escaneie o qr code para ter acesso a chave de segurança')
    qrkey.show()
'''FUNCAO PARA DESCRIPTOGRAFAR'''
def decrypt():
    recebekey = input('digite a chave de segurança: ')
    if recebekey == key:
        recebecodigo = input('digite o texto criptografado: ')
        codigo = open('C:/Users/kb/Desktop/python/APS/codigo.txt')
        lercodigo = codigo.readline()
        
        if lercodigo == recebecodigo:
            frase = open('C:/Users/kb/Desktop/python/APS/texto.txt')
            txtdecrypt = frase.readline()
            print('o texto descriptografado é: ', txtdecrypt)
            frase.close()
        
        else:
            print('texto criptografado errado')
        codigo.close()
    else:
        print('a chave de segurança não é valida')
