

class VendedorDto:
  def __init__(self, codigo, nome, cpf):
    self.__codigo = codigo
    self.__nome = nome
    self.__cpf = cpf

  @property
  def codigo(self):
    return self.__codigo

  @property
  def nome(self):
    return self.__nome

  @property
  def cpf(self):
    return self.__cpf

  def __repr__(self):
    return f'Codigo: {self.codigo}, Nome: {self.nome}, Cpf: {self.cpf}'