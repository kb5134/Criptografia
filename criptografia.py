#encoding:utf-8
import funcoes
c = 1
while c != 0: 
    print('-'*72)
    print(" digite encrypt para criptografar \n ou \n decrypt para descriptografar \n ou \n sair para encerar \n  ")
    print('-'*72)
    escolha = input()
    if escolha == 'encrypt':
        print('-'*72)
        funcoes.encrypt()
        funcoes.senha()
        funcoes.qrcode()
        print('-'*72)
    elif escolha == 'decrypt':
        print('-'*72)
        funcoes.decrypt()
        print('-'*72)
    elif escolha == 'sair':
        c = 0
    else:
        print('ERROR')
