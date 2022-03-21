#encoding:utf-8
import funcoes
c = 1
while c != 0: 
    print('-'*72)
    print(" digite 1 para criptografar \n ou \n 2 para descriptografar \n ou \n 0 para encerrar \n  ")
    print('-'*72)
    escolha = input()
    if escolha == '1':
        print('-'*72)
        funcoes.senha()
        funcoes.encrypt()
        funcoes.qrcode()
        print('-'*72)
    elif escolha == '2':
        print('-'*72)
        funcoes.decrypt()
        print('-'*72)
    elif escolha == '0':
        c = 0
    else:
        print('ERROR')
