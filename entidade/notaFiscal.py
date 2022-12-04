from excecoes.notaJahGeradaException import NotaJahGeradaException
from entidade.cliente import Cliente
from entidade.vendedor import Vendedor
from entidade.itemNotaFiscal import ItemNotaFiscal
from datetime import datetime


class NotaFiscal:
    def __init__(self, numero: int,
                 cliente: Cliente,
                 vendedor: Vendedor):

        self.__numero = numero
        self.__cliente = cliente
        self.__vendedor = vendedor
        self.__itens_da_nota = []
        self.__valor_total = 0.0
        self.__datetime = None

    @property
    def numero(self):
        return self.__numero

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
    def datetime(self) -> datetime:
        return self.__datetime

    @property
    def itens_da_nota(self):
        return self.__itens_da_nota

    def adicionar_item_nota_fiscal(self, dados_item_nota: dict):
        if self.__datetime:
            raise NotaJahGeradaException

        produto_nota = dados_item_nota["produto_item"]
        quantidade_nota = dados_item_nota["quantidade_item"]
        
        item_nota = ItemNotaFiscal(produto_nota, quantidade_nota)

        self.__itens_da_nota.append(item_nota)

    def excluir_item_nota_fiscal(self, posicao_item_nota: int):
        if self.__datetime:
            raise NotaJahGeradaException

        self.__itens_da_nota.pop(posicao_item_nota)

    def gerar_nota(self):
        self.__datetime = datetime.now()
        self.__calcular_valor_total()

    def __calcular_valor_total(self):
        total = 0.0
        for item_nota in self.__itens_da_nota:
            total += item_nota.calcular_valor_total()

        self.__valor_total = total
