from entidade.cliente import Cliente
from entidade.vendedor import Vendedor
from entidade.itemNotaFiscal import ItemNotaFiscal
from datetime import datetime


class NotaFiscal:
    def __init__(self, numero_nota: int,
                 cliente: Cliente,
                 vendedor: Vendedor):

        self.__numero_nota = numero_nota
        self.__cliente = cliente
        self.__vendedor = vendedor
        self.__itens_da_nota = []
        self.__valor_total = 0.0
        self.__datetime = None

    @property
    def numero_nota(self):
      return self.__numero_nota

    @property
    def cliente(self):
      return self.__cliente

    @property
    def vendedor(self):
      return self.__vendedor

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def data(self):
        return self.__datetime

    def adicionar_item_nota_fiscal(self, item_nota: ItemNotaFiscal):
      if self.__datetime:
        raise NotaJahGeradaException

      self.__itens_da_nota.append(item_nota)

    def excluir_item_nota_fiscal(self, item_nota: ItemNotaFiscal):
      if self.__datetime:
        raise NotaJahGeradaException

      self.__itens_da_nota.remove(item_nota)
    
    def gerar_nota(self):
      self.__datetime = datetime.now()
      self.__calcular_valor_total()
    
    def __calcular_valor_total(self):
      total = 0.0
      for item_nota in self.__itens_da_nota:
        total += item_nota.produto.valor
      
      self.__valor_total = total
