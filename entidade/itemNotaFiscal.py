
from entidade.abstractProduto import AbstractProduto
from excecoes.pesoInvalidoException import PesoInvalidoException
from excecoes.quantidadeInvalidaException import QuantidadeInvalidoException


class ItemNotaFiscal:
    def __init__(self, produto: AbstractProduto, quantidade: int):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__diminuir_estoque()
        self.__incrementar_quantidade_vendida()

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def calcular_valor_total(self):
        return self.__produto.calcular_preco_item(self.__quantidade)

    def __diminuir_estoque(self):
        self.__produto.diminuir_estoque(self.__quantidade)

    def __incrementar_quantidade_vendida(self):
        self.__produto.incrementar_quantidade_vendida(self.__quantidade)