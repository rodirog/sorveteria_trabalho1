from entidade.produto import Produto
from excecoes.pesoInvalidoException import PesoInvalidoException
from excecoes.quantidadeInvalidaException import QuantidadeInvalidoException


class ItemNotaFiscal:
    def __init__(self, produto: Produto, quantidade: int, peso: float):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__peso = peso
        self.__checar_unitario_ou_peso()
        self.__diminuir_estoque()
        self.__incrementar_somatorio_de_vendas()

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def peso(self):
        return self.__peso

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade
    
    def __checar_unitario_ou_peso(self):
        if self.__produto.tipo_produto == "Sorvete" and self.__quantidade != 1:
            raise QuantidadeInvalidoException
        if self.__produto.tipo_produto == "Bebida" and self.__peso != 1:
            raise PesoInvalidoException

    def calcular_valor_total(self):
        return self.__produto.calcular_preco_item(self.__quantidade, self.__peso)

    def __diminuir_estoque(self):
        self.__produto.diminuir_estoque(self.__quantidade, self.__peso)

    def __incrementar_somatorio_de_vendas(self):
        self.__produto.incrementar_somatorio_de_vendas(self.__quantidade, self.__peso)