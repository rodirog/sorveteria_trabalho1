

from abc import ABC, abstractmethod
import pickle


class PickleDAO(ABC):
  @abstractmethod
  def __init__(self, repositorio):
    self.__repositorio = repositorio
    self.__criar_arquivo_caso_nao_existe()
    # self.salvar([])

  @abstractmethod
  def adicionar(self, entidade, chave):
    entidades = self.carregar()

    item = (chave, entidade)
    entidades.append(item)

    self.salvar(entidades)

  @abstractmethod
  def encontrar(self, chave):
    entidades = self.carregar()

    return self.encontrar_entidade(entidades, chave)

  @abstractmethod
  def atualizar(self, entidade):
    entidades = self.carregar()

    entidade_encontrado = self.encontrar_entidade(entidades, entidade.cpf)

    entidade_encontrado.nome = entidade.nome
    entidade_encontrado.email = entidade.email
    entidade_encontrado.telefone = entidade.telefone

    self.salvar(entidades)

  @abstractmethod
  def remover(self, entidade):
    entidades = self.carregar()

    entidades.remove(entidade)

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

  def encontrar_entidade(self, itens, chave_buscada):
    for chave, entidade in itens:
      if chave == chave_buscada:
        return entidade