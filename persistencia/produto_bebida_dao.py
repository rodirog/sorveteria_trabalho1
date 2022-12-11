from entidade.produtoBebida import ProdutoBebida
from persistencia.dao import DAO


class ProdutoBebidaDAO(DAO):
    def __init__(self):
        super().__init__('bebidas')

    def adicionar(self, bebida: ProdutoBebida):
        super().adicionar(bebida)

    def encontrar(self, codigo):
        return super().encontrar(codigo)

    def remover(self, codigo):
        super().remover(codigo)

    def listar(self):
        return super().listar()

    def atualizar(self):
        pass