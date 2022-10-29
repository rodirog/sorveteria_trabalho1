from limite.telaLoja import TelaLoja
import sys
from controle.controladorFornecedor import ControladorFornecedor
from controle.controladorProduto import ControladorProduto
from controle.controladorCliente import ControladorCliente

class ControladorLoja:

    def __init__(self):
        self.__tela_principal = TelaLoja()
        self.__controlador_fornecedor = ControladorFornecedor(self)
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_cliente = ControladorCliente(self)
        #o self do parametro representa o parametro controlar_cliente no init de ControladorCliente

    def inicia_fornecedores(self):
        self.__controlador_fornecedor.mostra_tela_opcoes()
        self.__controlador_fornecedor.p

    def inicia_produtos(self):
        self.__controlador_produto.mostra_tela_opcoes()
        self.__controlador_produto.p

    def inicia_clientes(self):
        self.__controlador_cliente.mostrar_tela_opcoes()

    def inicia_notas_fiscais(self):
        print("NOTAS FISCAIS")

    def finaliza(self):
        sys.exit()

    def inicia(self):
        opcoes = {
            1: self.inicia_fornecedores,
            2: self.inicia_produtos,
            3: self.inicia_notas_fiscais,
            4: self.inicia_clientes,
            0: self.finaliza
        }

        while True:
            opcao = self.__tela_principal.mostra_tela_inicial()
            opcoes[opcao]()
