
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

