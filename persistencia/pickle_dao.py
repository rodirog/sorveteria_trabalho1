

from abc import ABC, abstractmethod
import pickle


class PickleDAO(ABC):
  @abstractmethod
  def __init__(self, repositorio):
    self.__repositorio = repositorio
    # self.salvar([])

  @abstractmethod
  def adicionar(self, entidade):
    entidades = self.carregar()

    entidades.append(entidade)

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
    entidades = []

    nome_arquivo = f'{self.__repositorio}.pkl'
    arquivo_entidades = open(nome_arquivo, 'rb')
    entidades = pickle.load(arquivo_entidades)
    arquivo_entidades.close()

    return entidades

  def salvar(self, entidades):
    nome_arquivo = f'{self.__repositorio}.pkl'
    arquivo_entidades = open(nome_arquivo, 'wb')

    pickle.dump(entidades, arquivo_entidades)
    arquivo_entidades.close()
  
  def encontrar_entidade(self, entidades, chave):
    for entidade in entidades:
      if entidade.cpf == chave:
        return entidade