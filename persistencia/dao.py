

from abc import ABC, abstractmethod


class DAO(ABC):
  @abstractmethod
  def __init__(self, nome_repositorio):
    self.__clientes = []

  @abstractmethod
  def adicionar(self, entidade):
    self.__clientes.append(entidade)

  @abstractmethod
  def encontrar(self, chave):
    for cliente in self.__clientes:
      if cliente.cpf == chave:
        return cliente

  @abstractmethod
  def atualizar(self, entidade):
    cliente_encontrado = self.encontrar(entidade.cpf)

    cliente_encontrado.nome = entidade.nome
    cliente_encontrado.email = entidade.email
    cliente_encontrado.telefone = entidade.telefone

  @abstractmethod
  def remover(self, entidade):
    self.__clientes.remove(entidade)

  @abstractmethod
  def listar(self):
    return self.__clientes