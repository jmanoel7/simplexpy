class Simplex:

	def __init__(self, otimizar='max', tabela=[ [0, 1, 2], [3, 4, 5] ]):
		self.__otimizar = otimizar
		self.__tabela = tabela

	@property
	def otimizar(self):
		return self.__otimizar

	@otimizar.setter
	def otimizar(self, otimizar):
		self.__otimizar = otimizar

	@property
	def tabela(self):
		return self.__tabela

	@tabela.setter
	def tabela(self, tabela):
		self.__tabela = tabela

	def __repr__(self):
		return ("SimplexPy(otimizar={0}, tabela={1})".format(self.__otimizar, self.__tabela))

	def __str__(self):
		return "({0}, {1})".format(self.__otimizar, self.__tabela)
