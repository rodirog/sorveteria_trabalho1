

# C Criar (create)
# R Ler/recuperar (read/retrive)
# U Atualizar (update)
# D Deletar/remover (delete)

from entidade.cliente import Cliente
from excecoes.clienteJahExisteException import ClienteJahExisteException
from excecoes.clienteNaoExisteException import ClienteNaoExisteException
from excecoes.cpfInvalidoException import CpfInvalidoException
from excecoes.objeto_vazio_exception import ObjetoVazioException
from persistencia.pickle_dao import PickleDAO


class ClienteDAO(PickleDAO):
  def __init__(self):
    super().__init__('clientes')

  def adicionar(self, cliente: Cliente):
    if not cliente or not cliente.cpf:
      raise ObjetoVazioException

    cliente_encontrado = self.encontrar(cliente.cpf)
    if cliente_encontrado:
        raise ClienteJahExisteException
    
    super().adicionar(cliente)

  def encontrar(self, cpf):
    if not cpf:
      raise ObjetoVazioException
    
    return super().encontrar(cpf)

  def atualizar(self, cliente: Cliente):
    if not cliente or not cliente.cpf:
      raise ObjetoVazioException

    cliente_encontrado = self.encontrar(cliente.cpf)
    if not cliente_encontrado:
        raise ClienteNaoExisteException
    
    super().atualizar(cliente)

  def remover(self, cpf):
    if not cpf:
      raise ObjetoVazioException

    cliente_encontrado = self.encontrar(cpf)
    if not cliente_encontrado:
        raise ClienteNaoExisteException

    super().remover(cliente_encontrado)

  def listar(self):
    return super().listar()