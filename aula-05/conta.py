
class Conta():
	def __init__(self, numero, titular, saldo, limite):
		self.__numero  = numero
		self.__titular = titular
		self.__saldo   = saldo
		self.__limite  = limite

	def sacar(self, valor):
		self.__saldo -= valor

	def depositar(self, valor):
		self.__saldo += valor

	def extrato(self):
		print(f'Titular: {self.__titular}\nSaldo: {self.__saldo}')

	def tranferir(self, valor, destino):
		self.sacar(valor)
		destino.depositar(valor)
 
	@property
	def saldo(self):
		return self.__saldo

	@property
	def titular(self):
		return self.__titular

	@property 
	def limite(self):
		return self.__limite

	@limite.setter
	def limite(self, limite):
		self.__limite = limite

conta = Conta(123, 'Lucas', 100, 1000)
conta2 = Conta(321, 'Marco', 1, 1000)

conta.tranferir(10, conta2)

assert ( 11 == conta2._Conta__saldo)
assert (90 == conta.saldo)
assert('Lucas' == conta.titular)
assert(1000 == conta.limite)


