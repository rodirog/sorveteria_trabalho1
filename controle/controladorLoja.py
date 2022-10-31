from limite.telaLoja import TelaLoja
import sys
from controle.controladorProduto import ControladorProduto
from controle.controladorCliente import ControladorCliente
from controle.controladorVendedor import ControladorVendedor
from controle.controladorNotaFiscal import ControladorNotaFiscal


class ControladorLoja:

    def __init__(self):
        self.__tela_principal = TelaLoja()
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_vendedor = ControladorVendedor(self)
        self.__controlador_nota_fiscal = ControladorNotaFiscal(
            self, self.__controlador_cliente, self.__controlador_vendedor, self.__controlador_produto)
        # o self do parametro representa o parametro controlar_cliente no init de ControladorCliente

    def iniciar_produtos(self):
        self.__controlador_produto.mostrar_tela_opcoes()
        # self.__controlador_produto.p

    def iniciar_clientes(self):
        self.__controlador_cliente.mostrar_tela_opcoes()
        # self.__controlador_cliente.p

    def iniciar_vendedores(self):
        self.__controlador_vendedor.mostrar_tela_opcoes()
        # self.__controlador_vendedor.p

    def iniciar_notas_fiscais(self):
        self.__controlador_nota_fiscal.mostrar_tela_opcoes()

    def finalizar(self):
        sys.exit()

    def iniciar(self):
        opcoes = {
            1: self.iniciar_produtos,
            2: self.iniciar_clientes,
            3: self.iniciar_vendedores,
            4: self.iniciar_notas_fiscais,
            0: self.finalizar
        }

        while True:
            try:
                opcao = self.__tela_principal.mostrar_tela_inicial()
                opcoes[opcao]()
            except KeyError:
                self.__tela_principal.mostrar_mensagem(
                    "Voce digitou um numero invalido.")
            except ValueError:
                self.__tela_principal.mostrar_mensagem(
                    "Voce digitou um tipo invalido.")
