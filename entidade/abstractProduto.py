
from abc import ABC, abstractmethod

class AbstractProduto(ABC):
    @abstractmethod
    def __init__(self, codigo, estoque, descricao, valor):
        if isinstance(codigo, int):
            self.__codigo = codigo

        if isinstance(estoque, int):
            self.__estoque = estoque

        if isinstance(descricao, str):
            self.__descricao = descricao

        if isinstance(valor, float):
            self.__valor = valor

    @abstractmethod
    def calcular_preco_item(self):
        pass 

    @abstractmethod    
    def diminuir_estoque(self):
        pass

    @abstractmethod
    def incrementar_quantidade_vendida(self):
        pass

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque):
        if isinstance(estoque, int | float):
            self.__estoque = estoque

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor

