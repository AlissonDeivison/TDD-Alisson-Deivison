class ContaBancaria:  # BankAccount
    def __init__(self, numero, nome, saldo=0.0):
        self.numero = numero
        self.nome = nome
        self.saldo = float(saldo)

    def depositar(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser maior que zero")
        self.saldo += valor
        
    def sacar(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Valor de saque deve ser maior que zero")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque")
        self.saldo -= valor
        
    def consultar_saldo(self):
        return self.saldo