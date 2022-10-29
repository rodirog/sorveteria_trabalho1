from produto import Produto


class ItemNotaFiscal:
    def __init__(self, produto: Produto, quantidade: int, peso: float):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__peso = peso

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