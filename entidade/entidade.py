from abc import ABC, abstractmethod


class Entidade(ABC):
  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def chave(self):
    pass