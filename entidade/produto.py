from excecoes.estoqueVazioException import EstoqueVazioException


class Produto:
    def __init__(self, codigo, estoque, descricao, tipo_produto, valor):
        if isinstance(codigo, int):
            self.__codigo = codigo

        if isinstance(estoque, int):
            self.__estoque = estoque

        if isinstance(descricao, str):
            self.__descricao = descricao

        if isinstance(tipo_produto, str):
            self.__tipo_produto = tipo_produto

        if isinstance(valor, float):
            self.__valor = valor
        
        self.__somatorio_de_vendas = 0

    def calcular_preco_item(self, quantidade, peso):
        return (self.__valor * peso) * quantidade

    def diminuir_estoque(self, quantidade, peso):
        if self.__tipo_produto == "Sorvete":
            if self.__estoque - peso < 0:
                raise EstoqueVazioException
            else:
                self.__estoque -= peso
        else:
            if self.__estoque - quantidade < 0:
                raise EstoqueVazioException
            else:
                self.__estoque -= quantidade

    def incrementar_somatorio_de_vendas(self, quantidade, peso):
        if self.__tipo_produto == "Bebida":
            self.__somatorio_de_vendas += quantidade
        else:
            self.__somatorio_de_vendas += peso

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
        if isinstance(estoque, int):
            self.__estoque = estoque

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def tipo_produto(self):
        return self.__tipo_produto

    @tipo_produto.setter
    def tipo_produto(self, tipo_produto):
        if isinstance(tipo_produto, str):
            self.__tipo_produto = tipo_produto

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def somatorio_de_vendas(self):
        return self.__somatorio_de_vendas