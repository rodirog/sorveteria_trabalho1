# import pickle
# from persistencia.abstractDAO import DAO
# from entidade.produtoSorvete import ProdutoSorvete


# class SorveteDAO(DAO):
# 	def __init__(self):
# 		super().__init__('sorvetes.pkl')

# 	def add(self, sorvete: ProdutoSorvete):
# 		if (isinstance(sorvete.codigo, int)) and (sorvete is not None) \
# 			and isinstance(sorvete, ProdutoSorvete):
# 			super().add(sorvete.codigo, sorvete)

# 	def get(self, key: int):
# 		if isinstance(key, int):
# 			return super().get(key)

# 	def remove(self, key: int):
# 		if isinstance(key, int):
# 			return super().remove(key)

from entidade.produtoSorvete import ProdutoSorvete
from persistencia.dao import DAO


class ProdutoSorveteDAO(DAO):
    def __init__(self):
        super().__init__('sorvetes')

    def adicionar(self, sorvete: ProdutoSorvete):
        super().adicionar(sorvete)

    def encontrar(self, codigo):
        return super().encontrar(codigo)

    def remover(self, codigo):
        super().remover(codigo)

    def listar(self):
        return super().listar()

    def atualizar(self):
        pass

