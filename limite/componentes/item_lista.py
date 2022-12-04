

class ItemLista:
  def __init__(self, nome, cpf):
    self.__nome = nome
    self.__cpf = cpf

  @property
  def cpf(self):
    return self.__cpf
  
  def __repr__(self) -> str:
    return f'{self.__nome}'