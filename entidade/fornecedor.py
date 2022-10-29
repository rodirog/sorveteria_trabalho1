from entidade import abstractPessoa


class Fornecedor(abstractPessoa):
    def __init__(self, nome, cnpj, telefone):
        super.__init__(nome)
        self.__cnpj = cnpj
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def telefone(self):
        return self.__telefone
