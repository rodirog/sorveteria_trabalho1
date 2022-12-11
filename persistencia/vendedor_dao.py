
# C Criar (create)
# R Ler/recuperar (read/retrive)
# U Atualizar (update)
# D Deletar/remover (delete)

from entidade.vendedor import Vendedor
from excecoes.vendedorJahExisteException import VendedorJahExisteException
from excecoes.vendedorNaoExisteException import VendedorNaoExisteException
from excecoes.cpfInvalidoException import CpfInvalidoException
from excecoes.objeto_vazio_exception import ObjetoVazioException
from persistencia.dao import DAO


class VendedorDAO(DAO):
  def __init__(self):
    super().__init__('vendedores')
    self.__codigo = 1

  def adicionar(self, vendedor: Vendedor):
    if not vendedor or not vendedor.cpf:
      raise ObjetoVazioException

    vendedor_encontrado = self.__encontrar_por_cpf(vendedor.cpf)
    if vendedor_encontrado:
        raise VendedorJahExisteException
    
    vendedor.codigo = self.__codigo
    self.__codigo += 1

    super().adicionar(vendedor)

  def encontrar(self, codigo: int):
    if not codigo:
      raise ObjetoVazioException
    
    return super().encontrar(codigo)

  def atualizar(self, vendedor: Vendedor):
    if not vendedor or not vendedor.codigo:
      raise ObjetoVazioException

    vendedor_encontrado = self.encontrar(vendedor.codigo)
    if not vendedor_encontrado:
        raise VendedorNaoExisteException
    
    super().atualizar(vendedor)

  def remover(self, codigo: int):
    if not codigo:
      raise ObjetoVazioException

    super().remover(codigo)

  def listar(self):
    return super().listar()

  def __encontrar_por_cpf(self, cpf):
    if not cpf:
      raise ObjetoVazioException
    
    return super().encontrar(cpf)

 