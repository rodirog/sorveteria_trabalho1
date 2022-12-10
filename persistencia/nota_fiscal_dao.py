from entidade.notaFiscal import NotaFiscal
from persistencia.dao import DAO


class NotaFiscalDAO(DAO):
    def __init__(self):
        super().__init__('notas_fiscais')

    def adicionar(self, nota_fiscal: NotaFiscal):
        super().adicionar(nota_fiscal)

    def encontrar(self, numero):
        return super().encontrar(numero)

    def remover(self, numero):
        super().remover(numero)

    def listar(self):
        return super().listar()

    def atualizar(self):
        pass