from entidade.pessoaFisica import PessoaFisica


class Vendedor(PessoaFisica):
    def __init__(self, nome: str, cpf: str, codigo_vendedor: int):
        super().__init__(nome, cpf)
        self.__codigo_vendedor = codigo_vendedor

    @property
    def codigo_vendedor(self):
        return self.__codigo_vendedor
