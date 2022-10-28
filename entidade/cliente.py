from entidade.pessoaFisica import PessoaFisica


class Cliente(PessoaFisica):
  def __init__(self, nome: str, cpf: str, email: str, telefone: str):
    super().__init__(nome, cpf)
    self.__email = email
    self.__telefone = telefone

  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self, email:str):
    self.__email = email

  @property
  def telefone(self):
    return self.__telefone

  @telefone.setter
  def telefone(self, telefone: str):
     self.__telefone = telefone
