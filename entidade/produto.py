
class Produto:
    def __init__(self, codigo, quantidade, descricao, tipo_produto, valor):
        if isinstance(codigo, int):
            self.__codigo = codigo
    
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        
        if isinstance(descricao, str):
            self.__descricao = descricao
        
        if isinstance(tipo_produto, str):
            self.__tipo_produto = tipo_produto
       
        if isinstance(valor, float):
            self.__valor = valor 

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
      
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
      