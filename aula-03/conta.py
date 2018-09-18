
class Conta():
	def __init__(self, numero, titular, saldo, limite):
		self.numero  = numero
		self.titular = titular
		self.saldo   = saldo
		self.limite  = limite

	def sacar(self, valor):
		self.saldo -= valor

	def depositar(self, valor):
		self.saldo += valor

	def extrato(self):
		print(f'Titular: {self.titular}\nSaldo: {self.saldo}')