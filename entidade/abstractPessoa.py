from abc import ABC, abstractmethod


class AbstractPessoa(ABC):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

#copiar o abstractPessoa certo da yaskara
    