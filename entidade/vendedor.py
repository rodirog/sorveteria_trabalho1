from entidade.pessoaFisica import PessoaFisica


class Vendedor(PessoaFisica):
    def __init__(self, nome: str, cpf: int, codigo: int):
        super().__init__(nome, cpf)
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo
