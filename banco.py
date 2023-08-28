import textwrap

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso.")
    else:
        print("\nOperação falhou. Valor informado é inválido")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente")
    elif excedeu_saque:
        print("\nOperação falhou! Número de saques excedido")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso.")
    else:
        print("\nOperação falhou! O valor informado é inválido")
    return saldo, extrato, numero_saques

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe usuário com esse CPF")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: \t{conta['agencia']}
        C/C: \t\t{conta['numero_conta']}
        Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def menu():
    print("\nOpções:")
    print("d - Depositar")
    print("s - Sacar")
    print("e - Exibir Extrato")
    print("nu - Novo Usuário")
    print("nc - Nova Conta")
    print("lc - Listar Contas")
    print("q - Sair")
    return input("Escolha uma opção: ")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            print(extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada")

if __name__ == "__main__":
    main()
