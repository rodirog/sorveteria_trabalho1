from abc import ABC, abstractmethod


class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        pass