from abc import ABC, abstractmethod


class Entidade(ABC):
  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  # @property
  def chave(self):
    pass