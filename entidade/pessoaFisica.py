from abc import abstractmethod
from entidade.abstractPessoa import AbstractPessoa


class PessoaFisica(AbstractPessoa):
    @abstractmethod
    def __init__(self, nome: str, cpf: int):
        super().__init__(nome)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
