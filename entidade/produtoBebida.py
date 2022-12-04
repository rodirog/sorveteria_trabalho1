
from excecoes.estoqueVazioException import EstoqueVazioException
from entidade.abstractProduto import AbstractProduto

class ProdutoBebida(AbstractProduto):
    def __init__(self, codigo, estoque, descricao, valor):
        super().__init__(codigo, estoque, descricao, valor)
        self.__tipo = 2
        self.__quantidade_vendida = 0

    def calcular_preco_item(self, quantidade):
        return (self.valor * quantidade)

    def diminuir_estoque(self, quantidade):
        if self.estoque - quantidade < 0:
            raise EstoqueVazioException
        else:
            self.estoque -= quantidade

    def incrementar_quantidade_vendida(self, quantidade):
        self.__quantidade_vendida += quantidade
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def quantidade_vendida(self):
        return self.__quantidade_vendida

    