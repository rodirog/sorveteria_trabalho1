from entidade.abstract_pessoa import AbstractPessoa
from entidade.entidade import Entidade


class Cliente(AbstractPessoa, Entidade):
  def __init__(self, nome: str, cpf: int, email: str, telefone: str):
    super().__init__(nome, cpf)
    self.__email = email
    self.__telefone = telefone

  @property
  def chave(self):
    return self.cpf

  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self, email: str):
    self.__email = email

  @property
  def telefone(self):
    return self.__telefone

  @telefone.setter
  def telefone(self, telefone: str):
    self.__telefone = telefone
