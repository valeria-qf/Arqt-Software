
class Desconto (ABC):
		@abstractmethod
		def calcular_desconto (self):
			pass

class Fixo(Desconto):
			def __init__(self):
				pass
		def calcular_desconto(self):
			return preco – 10

class Porcentagem(Desconto):
			def __init__(self):
				pass
		def calcular_desconto(self):
			return preco * 0.90

class CalculadoraDesconto:
	def __init__(self, tipo_desconto):
		self.tipo_desconto = tipo_desconto
	def calcular_desconto_total(self):
		if self.tipo_desconto:
			return self.tipo_desconto.calcular_desconto()
		else:
					return preco
