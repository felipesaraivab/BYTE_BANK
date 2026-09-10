# ByteBank - Nivel 1 (MVP)
# Sprint 1: sistema bancario basico com menu interativo.
# Operacoes: Consultar Saldo, Depositar, Sacar e Sair.

# O saldo comeca zerado. Vou guardar ele numa variavel simples por enquanto
# (nos proximos sprints isso vira uma estrutura de dados maior, tipo dicionario/matriz).
saldo = 0.0

print("=== ByteBank MVP ===")

# Loop principal do menu. Ele fica rodando ate o usuario escolher a opcao de Sair.
rodando = True

while rodando:
    print()
    print("[1] Consultar Saldo")
    print("[2] Depositar")
    print("[3] Sacar")
    print("[4] Sair")

    opcao = input("> Digite a operacao desejada: ")

    if opcao == "1":
        # Consultar Saldo: so mostra o valor atual, nao mexe em nada.
        print(f"Seu saldo atual e: R$ {saldo:.2f}")

    elif opcao == "2":
        # Depositar: precisa bloquear valores negativos ou zero.
        valor = float(input("Digite o valor do deposito: "))

        if valor <= 0:
            print("Erro: o valor do deposito precisa ser maior que zero.")
        else:
            saldo += valor
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")

    elif opcao == "3":
        # Sacar: precisa bloquear valores negativos/zero E bloquear saldo insuficiente.
        valor = float(input("Digite o valor do saque: "))

        if valor <= 0:
            print("Erro: o valor do saque precisa ser maior que zero.")
        elif valor > saldo:
            print("Erro: saldo insuficiente para realizar esse saque.")
        else:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        # Sair: encerra o loop.
        print("Encerrando o ByteBank. Ate mais!")
        rodando = False

    else:
        # Qualquer digitacao fora de 1-4 cai aqui.
        print("Opcao invalida. Escolha um numero de 1 a 4.")