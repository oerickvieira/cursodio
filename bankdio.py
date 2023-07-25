menu = """

[1]Deposito
[2]Saque
[3]Extrato
[4]Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite de saque")

        elif excedeu_saque:
            print("Operação falhou! O valor do saque excedeu o numero de saque")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é invalido.")
            
        
    elif opcao == "3":
        print("\n=================Extrato=================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=========================================")

    elif opcao == "4":
        break

    else:
        print("Operação invalida, tente novamente")
        
