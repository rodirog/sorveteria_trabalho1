class Produto:
    def __init__(self, codigo, quantidade, descricao):
        self.__codigo = codigo
        self.__quantidade = quantidade
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def descricao(self):
        return self.__descricao