
from entidade import abstractPessoa


class Fornecedor(abstractPessoa.AbstractPessoa):
    def __init__(self, nome, cnpj, telefone):
        super().__init__(nome)
        self.__cnpj = cnpj
        self.__telefone = telefone

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
        
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone