

# C Criar (create)
# R Ler/recuperar (read/retrive)
# U Atualizar (update)
# D Deletar/remover (delete)

from entidade.cliente import Cliente
from excecoes.clienteJahExisteException import ClienteJahExisteException
from excecoes.clienteNaoExisteException import ClienteNaoExisteException
from excecoes.objeto_vazio_exception import ObjetoVazioException
from persistencia.dao import DAO


class ClienteDAO(DAO):
  def __init__(self):
    super().__init__('clientes')

  def adicionar(self, cliente: Cliente):
    if not cliente or not cliente.cpf:
      raise ObjetoVazioException

    cliente_encontrado = self.encontrar(cliente.cpf)
    if cliente_encontrado:
        raise ClienteJahExisteException
    
    super().adicionar(cliente)

  def encontrar(self, cpf: int):
    if not cpf:
      raise ObjetoVazioException
    
    return super().encontrar(cpf)

  def atualizar(self, cliente: Cliente):
    if not cliente or not cliente.cpf:
      raise ObjetoVazioException

    cliente_encontrado = self.encontrar(cliente.cpf)
    if not cliente_encontrado:
        raise ClienteNaoExisteException
    
    cliente_encontrado.nome = cliente.nome
    cliente_encontrado.email = cliente.email
    cliente_encontrado.telefone = cliente.telefone

    super().atualizar(cliente)

  def remover(self, cpf: int):
    if not cpf:
      raise ObjetoVazioException

    super().remover(cpf)

  def listar(self):
    return super().listar()
  
