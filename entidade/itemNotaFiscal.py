from entidade.produto import Produto


class ItemNotaFiscal:
    def __init__(self, produto: Produto, quantidade: int, peso: float):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__peso = peso
        self.__diminuir_estoque()

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

    def calcular_valor_total(self):
        return self.__produto.calcular_preco_item(self.__quantidade, self.__peso)

    def __diminuir_estoque(self):
        self.__produto.diminuir_estoque(self.__quantidade, self.__peso)
