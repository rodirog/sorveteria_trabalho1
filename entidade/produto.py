
class Produto:
    def __init__(self, codigo, quantidade, descricao, tipo_produto):
        self.__codigo = codigo
        self.__quantidade = quantidade
        self.__descricao = descricao
        self.__tipo_produto = tipo_produto

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def tipo_produto(self):
        return self.__tipo_produto
    
    @tipo_produto.setter
    def tipo_produto(self, tipo_produto):
        self.__tipo_produto = tipo_produto
