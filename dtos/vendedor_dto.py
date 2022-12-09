

class VendedorDto:
  def __init__(self, nome: str, cpf: str = None, codigo: int = None):
    self.__nome = nome
    self.__cpf = cpf
    self.__codigo = codigo

  @property
  def nome(self):
    return self.__nome

  @property
  def cpf(self):
    return self.__cpf
  
  @property
  def codigo(self):
    return self.__codigo

  def __repr__(self):
    return f'Codigo: {self.codigo}\t, Nome: {self.nome}\t, Cpf: {self.cpf}\t'