

from abc import ABC, abstractmethod
import pickle

from entidade.entidade import Entidade
from excecoes.entidadeNaoExisteException import EntidadeNaoExisteException


class DAO(ABC):
  @abstractmethod
  def __init__(self, repositorio):
    self.__repositorio = repositorio
    self.__criar_arquivo_caso_nao_existe()

  @abstractmethod
  def adicionar(self, entidade: Entidade):
    entidades = self.carregar()

    entidades.append(entidade)

    self.salvar(entidades)

  @abstractmethod
  def encontrar(self, chave):
    entidades = self.carregar()

    return self.encontrar_entidade(entidades, chave)

  @abstractmethod
  def atualizar(self, entidade: Entidade):
    entidades = self.carregar()

    entidade_antiga = self.encontrar_entidade(entidades, entidade.chave)
    entidades.remove(entidade_antiga)
    entidades.append(entidade)

    self.salvar(entidades)

  @abstractmethod
  def remover(self, chave: int):
    entidades = self.carregar()

    entidade_encontrada = self.encontrar_entidade(entidades, chave)
    if not entidade_encontrada:
      raise EntidadeNaoExisteException

    entidades.remove(entidade_encontrada)

    self.salvar(entidades)

  @abstractmethod
  def listar(self):
    entidades = self.carregar()

    return entidades

  def carregar(self):
    itens = []

    nome_arquivo = f'{self.__repositorio}.pkl'
    arquivo = open(nome_arquivo, 'rb')
    itens = pickle.load(arquivo)
    arquivo.close()

    return itens

  def salvar(self, itens):
    nome_arquivo = f'{self.__repositorio}.pkl'
    arquivo = open(nome_arquivo, 'wb')

    pickle.dump(itens, arquivo)
    arquivo.close()

  def __criar_arquivo_caso_nao_existe(self):
    try:
      self.carregar()
    except FileNotFoundError:
      self.salvar([])

  def encontrar_entidade(self, entidades, chave: int):
    for entidade in entidades:
      if entidade.chave == chave:
        return entidade
