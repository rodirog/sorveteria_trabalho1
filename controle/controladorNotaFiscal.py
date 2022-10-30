from limite.telaNotaFiscal import TelaNotaFiscal
from entidade.notaFiscal import NotaFiscal


class ControladorNotaFiscal:
    def __init__(self, controlador_principal):
        #self.__controlador_principal = controlador_principal
        self.__tela_nota_fiscal = TelaNotaFiscal()
        self.__notaFiscal = []

    def adicionar_item_nota_fiscal(self):
        pass

    def excluir_item_nota_fiscal(self):
        pass

    def encontrar_nota_fiscal(self):
        pass

    def mostrar_tela_opcoes(self):
        opcoes = {
            1: self.adicionar_item_nota_fiscal,
            2: self.excluir_item_nota_fiscal,
            3: self.encontrar_nota_fiscal
        }
