
from excecoes.estoqueVazioException import EstoqueVazioException
from entidade.abstractProduto import AbstractProduto
from entidade.entidade import Entidade

class ProdutoSorvete(AbstractProduto, Entidade):
    def __init__(self, codigo, estoque, descricao, valor):
        super().__init__(codigo, estoque, descricao, valor)
        self.__tipo = 1 
        self.__quantidade_vendida = 0

    def calcular_preco_item(self, peso):
        return (self.valor * peso) 
    
    def retornar_ao_estoque(self, quantidade):
        self.estoque += quantidade
        self.__quantidade_vendida -= quantidade

    def diminuir_estoque(self, peso):
        if self.estoque - peso < 0:
            raise EstoqueVazioException
        else:
            self.estoque -= peso

    def incrementar_quantidade_vendida(self, peso):
        self.__quantidade_vendida += peso

    @property
    def tipo(self):
        return self.__tipo

    @property
    def quantidade_vendida(self):
        return self.__quantidade_vendida

    @property
    def chave(self):
        return self.codigo
