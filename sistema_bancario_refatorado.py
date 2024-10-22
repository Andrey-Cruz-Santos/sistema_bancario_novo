class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
                return True
            else:
                print("Saldo insuficiente para saque.")
                return False
        else:
            print("O valor de saque deve ser positivo.")
            return False

    def exibir_extrato(self):
        print(f"Extrato da conta {self.numero} (Titular: {self.titular}):")
        print(f"Saldo atual: R${self.saldo}")

class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, numero, titular, saldo_inicial=0):
        conta = Conta(numero, titular, saldo_inicial)
        self.contas.append(conta)
        return conta

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def depositar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    def sacar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

    def exibir_extrato(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            conta.exibir_extrato()
        else:
            print("Conta não encontrada.")

# Exemplo de uso
banco = Banco()

# Criação de contas
conta1 = banco.criar_conta(1, 'Alice', 1000)
conta2 = banco.criar_conta(2, 'Bob', 500)

# Operações
banco.depositar(1, 200)
banco.sacar(1, 100)
banco.exibir_extrato(1)

banco.depositar(2, 150)
banco.sacar(2, 700)
banco.exibir_extrato(2)
