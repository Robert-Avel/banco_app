import banco_conta, meu_modulo
from time import sleep
import os

bancos : list[banco_conta.Banco] = meu_modulo.loadfile('data.py')
meu_modulo.savefile('data.py', bancos)

while True:
    meu_modulo.optiontable(
        'Sistema Bancário',
        'Ver Cliente',
        'Ver Bancos',
        'Cadastro de Banco',
        'Cadastrar Cliente',
        'Fechar Conta',
        'Acessar Conta',
        'Editar Cadastro de Cliente',
        'Sair', center=True
    )
    option = meu_modulo.inputInt('Opção: ')
    
    if option == 1:
        if not meu_modulo.checktruty(bancos, 'Não exitem bancos cadastrados'): continue
        for b in bancos:
            print(b)
            if not meu_modulo.checktruty(b.contas, f'---> Não existem contas abertas no Banco "{b.nome}"'): continue
            for c in b.contas:
                print('--->', c)
    
    elif option == 2:
        if not meu_modulo.checktruty(bancos, 'Não exitem bancos cadastrados'): continue
        for b in bancos:
            print(b)

    elif option == 3:
        print('------ CADASTRAR BANCO ------')
        new_bank = str(input('Nome: '))
        bancos.append(banco_conta.Banco(new_bank))
    
    elif option == 4:
        print('------ CADASTRAR CLIENTE ------')
        if not meu_modulo.checktruty(bancos, 'Não exitem bancos cadastrados'): continue
        nome = str(input('Nome: '))
        idade = meu_modulo.inputInt('Idade: ')
        conta_tipo = str(input('Tipo de Conta: '))
        for n, b in enumerate(bancos):
            print(f'[ {n} ] - {b}')
        banco = meu_modulo.inputRange('Escolha o banco: ', bancos)
        bancos[banco].cadastrar_cliente(nome, idade, conta_tipo)

    elif option == 5:
        print('------ FECHAR UMA CONTA ------')
        for n, b in enumerate(bancos):
            print(f'[ {n} ] - {b}')
        banco = meu_modulo.inputInt('Escolha o banco: ')
        bancos[banco].fechar_conta()

    elif option == 6:
        if not meu_modulo.checktruty(bancos, 'Não exitem bancos cadastrados'): continue
        for n, b in enumerate(bancos):
            print(f'[ {n} ] - {b}')
        banco = meu_modulo.inputRange('Escolha o Banco: ', bancos)
        if not meu_modulo.checktruty(bancos[banco].contas, f'---> Não existem contas abertas no Banco "{bancos[banco].nome}"'): continue
        for n, c in enumerate(bancos[banco].contas):
            print(f'[ {n} ] - {c}')
        accont = meu_modulo.inputRange('Acessar conta: ', bancos[banco].contas)
        accont_acess: banco_conta.Conta = bancos[banco].contas[accont].conta

        while True:
            meu_modulo.optiontable(
                str(accont_acess),
                'Sacar', 'Depositar', 'Sair'
            )
            option = meu_modulo.inputInt('Opção: ')
            if option == 1:
                valor = float(input('Valor do saque: R$'))
                accont_acess.sacar(valor)
            if option == 2:
                valor = float(input('Valor do deposito: R$'))
                accont_acess.depositar(valor)
            elif option == 3:
                break

    elif option == 7:
        print('------ EDITAR UM CADASTRO ------')
        if not meu_modulo.checktruty(bancos, 'Não exitem bancos cadastrados'): continue
        for n, b in enumerate(bancos):
            print(f'[ {n} ] - {b}')
        banco = meu_modulo.inputRange('Escolha o Banco: ', bancos)
        bancos[banco].editar_conta()

    elif option == 8:
        break
    sleep(2)
    os.system('cls')

meu_modulo.savefile('data.py', bancos)