import random

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"
        else:
            return "Saldo insuficiente."

    def consultar_saldo(self):
        return f"Número da Conta: {self.numero}, Saldo: R${self.saldo}"

class Banco:
    def __init__(self):
        self.clientes = {}
        self.contas = {}

    def gerar_numero_conta(self):
        # Gera um número de conta único de 6 dígitos
        return str(random.randint(100000, 999999))

    def adicionar_cliente(self, nome, cpf):
        if cpf in self.clientes:
            return "Cliente já existe."
        else:
            cliente = Cliente(nome, cpf)
            self.clientes[cpf] = cliente
            # Criando uma nova conta para o cliente
            numero_conta = self.gerar_numero_conta()
            conta = Conta(numero_conta, cliente)
            self.contas[numero_conta] = conta
            return f"Cliente {nome} adicionado com sucesso. Número da Conta: {numero_conta}"

    def consultar_saldo_por_cpf(self, cpf):
        contas_cliente = [conta for conta in self.contas.values() if conta.cliente.cpf == cpf]
        if contas_cliente:
            for conta in contas_cliente:
                print(conta.consultar_saldo())
        else:
            return "Cliente não encontrado ou sem contas associadas."

    def realizar_deposito(self, cpf, valor):
        contas_cliente = [conta for conta in self.contas.values() if conta.cliente.cpf == cpf]
        if contas_cliente:
            conta = contas_cliente[0]  # Usamos a primeira conta encontrada
            return conta.depositar(valor)
        else:
            return "Cliente não encontrado ou sem contas associadas."

    def realizar_saque(self, cpf, valor):
        contas_cliente = [conta for conta in self.contas.values() if conta.cliente.cpf == cpf]
        if contas_cliente:
            conta = contas_cliente[0]  # Usamos a primeira conta encontrada
            return conta.sacar(valor)
        else:
            return "Cliente não encontrado ou sem contas associadas."

# Simulação de um app bancário
def menu():
    banco = Banco()
    
    while True:
        print("\n--- Menu do Banco ---")
        print("1. Adicionar Cliente e Criar Conta")
        print("2. Consultar Saldo por CPF")
        print("3. Realizar Depósito")
        print("4. Realizar Saque")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            print(banco.adicionar_cliente(nome, cpf))

        elif opcao == "2":
            cpf = input("Digite o CPF do cliente: ")
            resultado = banco.consultar_saldo_por_cpf(cpf)
            if resultado:
                print(resultado)

        elif opcao == "3":
            cpf = input("Digite o CPF do cliente: ")
            valor = float(input("Digite o valor do depósito: "))
            print(banco.realizar_deposito(cpf, valor))

        elif opcao == "4":
            cpf = input("Digite o CPF do cliente: ")
            valor = float(input("Digite o valor do saque: "))
            print(banco.realizar_saque(cpf, valor))

        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o aplicativo bancário
menu()
1
