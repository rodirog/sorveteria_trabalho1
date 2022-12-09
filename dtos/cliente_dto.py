

class ClienteDto:
  def __init__(self, nome: str, email: str, telefone: str, cpf: int = None):
    self.__nome = nome
    self.__cpf = cpf
    self.__email = email
    self.__telefone = telefone

  @property
  def nome(self):
    return self.__nome

  @property
  def cpf(self):
    return self.__cpf

  @property
  def email(self):
    return self.__email

  @property
  def telefone(self):
    return self.__telefone

  def __repr__(self):
    return f'Nome: {self.nome}\t, Cpf: {self.cpf}\t, Email: {self.email}\t, Telefone: {self.telefone}'