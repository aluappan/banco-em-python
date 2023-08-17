menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 5

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
        else:
            print("Operação falhou. O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedidos = qtd_saques >= LIMITE_SAQUES
        
        if saldo_excedido:
            print("Operação falhou. Você não tem saldo suficiente.")
        elif limite_excedido:
            print("Operação falhou. Você não tem limite.")
        elif saques_excedidos:
            print("Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtd_saques += 1
        else:
            print("Operação falhou. O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n============ EXTRATO ===========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
