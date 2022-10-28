from limite.telaLoja import TelaLoja
import sys
from controle.controladorFornecedor import ControladorFornecedor
from controle.controladorProduto import ControladorProduto
from controle.controladorCliente import ControladorCliente
from controle.controladorVendedor import ControladorVendedor

class ControladorLoja:

    def __init__(self):
        self.__tela_principal = TelaLoja()
        self.__controlador_fornecedor = ControladorFornecedor(self)
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_vendedor = ControladorVendedor(self)
        #o self do parametro representa o parametro controlar_cliente no init de ControladorCliente

    def iniciar_fornecedores(self):
        self.__controlador_fornecedor.mostrar_tela_opcoes()
        #self.__controlador_fornecedor.p

    def iniciar_produtos(self):
        self.__controlador_produto.mostrar_tela_opcoes()
        #self.__controlador_produto.p

    def iniciar_clientes(self):
        self.__controlador_cliente.mostrar_tela_opcoes()
        #self.__controlador_cliente.p

    def iniciar_vendedores(self):
        self.__controlador_vendedor.mostrar_tela_opcoes()
        #self.__controlador_vendedor.p

    def iniciar_notas_fiscais(self):
        print("NOTAS FISCAIS")

    def finalizar(self):
        sys.exit()

    def iniciar(self):
        opcoes = {1: self.iniciar_fornecedores, 2: self.iniciar_produtos, 3: self.iniciar_clientes, 4: self.iniciar_vendedores, 5: self.iniciar_notas_fiscais, 0: self.finalizar}

        while True:
            opcao = self.__tela_principal.mostrar_tela_inicial()
            opcoes[opcao]()
