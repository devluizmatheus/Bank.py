menu = ''' 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  '''

saldo = 0
limite = 500    
extrato = ""
numero_saques = 0 
LIMITE_DE_SAQUES = 3

while True:
    try:
        opcao = input(menu)

        if opcao == "d":
            depositando = float(input('''
===========================================
Insira o Valor do depósito:
                            
=> '''))

            saldo += depositando
    except ValueError:
        print('Insira apenas numeros')
            
    try:
        if opcao == "s":
            sacando = float(input(
'''
===========================================
Insira o Valor que deseja sacar:
                        
=>  '''))
            numero_saques += 1

            if sacando > limite:
                print(f'Operação falhou... O número de limite é de R$ {500:.2f}')
            
            if numero_saques > LIMITE_DE_SAQUES:
                print('Limite de Saque Diário alcançado.')

            else:
                saldo -= sacando
    except ValueError:
        print('Digite apenas números')

    if opcao == "e":
        print(
f'''
==========================================================
Saldo = R$ {saldo:.2f}
Limite = R$ {limite:.2f}
Numeros de Saques Restantes = {LIMITE_DE_SAQUES - numero_saques} 
============================================================''')
    elif opcao == "q":
        exit()

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')