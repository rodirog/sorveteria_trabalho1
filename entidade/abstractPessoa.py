from abc import ABC, abstractmethod


class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.__nome = nome

    @abstractmethod
    @property
    def nome(self):
        pass