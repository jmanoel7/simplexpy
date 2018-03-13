class Simplex:

	def __init__(self, otimizar='max', vars_decisao=2, tabela=[ [1, -3, -2, 0, 0, 0, 0], [0, 1, 1, 1, 0, 6, 3], [0, 5, 2, 0, 1, 20, 4] ]):
		self.__otimizar = otimizar
		self.__vars_decisao = vars_decisao
		self.__tabela = tabela

	@property
	def otimizar(self):
		return self.__otimizar

	@otimizar.setter
	def otimizar(self, otimizar):
		self.__otimizar = otimizar

	@property
	def vars_decisao(self):
		return self.__vars_decisao

	@vars_decisao.setter
	def vars_decisao(self, vars_decisao):
		self.__vars_decisao = vars_decisao

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

	def forma_padrao(self):
		pass

	def solucao(self):
		while True:
			sbf = {}
			vb = 
			vnb = 
			for i in range(0, self.__vars_decisao):
				item = {vnb[i]: 0}
				sbf.update(item)
			for i in range(1, len(self.__tabela):
				item = {vb[i]: tabela[i][-2]}
				sbf.update(item)
			if solucao_otima:
				break
			# troca de variaveis e atualizacao da tabela
