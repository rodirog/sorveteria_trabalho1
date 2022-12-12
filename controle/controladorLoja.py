from limite.telaLoja import TelaLoja
import sys
from controle.controladorSorvete import ControladorSorvete
from controle.controladorBebida import ControladorBebida
from controle.controladorCliente import ControladorCliente
from controle.controladorVendedor import ControladorVendedor
from controle.controladorNotaFiscal import ControladorNotaFiscal


class ControladorLoja:

    def __init__(self):
        self.__tela_principal = TelaLoja()
        self.__controlador_sorvete = ControladorSorvete()
        self.__controlador_bebida = ControladorBebida()
        self.__controlador_cliente = ControladorCliente()
        self.__controlador_vendedor = ControladorVendedor()
        self.__controlador_nota_fiscal = ControladorNotaFiscal(
            self.__controlador_cliente, self.__controlador_vendedor, 
            self.__controlador_sorvete, self.__controlador_bebida)

    def iniciar_sorvetes(self):
        self.__controlador_sorvete.mostrar_tela_opcoes()

    def iniciar_bebidas(self):
        self.__controlador_bebida.mostrar_tela_opcoes()

    def iniciar_clientes(self):
        self.__controlador_cliente.mostrar_tela_opcoes()

    def iniciar_vendedores(self):
        self.__controlador_vendedor.mostrar_tela_opcoes()

    def iniciar_notas_fiscais(self):
        self.__controlador_nota_fiscal.mostrar_tela_opcoes()

    def finalizar(self):
        sys.exit()

    def iniciar(self):
        lista_opcoes = {
            1: self.iniciar_sorvetes,
            2: self.iniciar_bebidas,
            3: self.iniciar_clientes,
            4: self.iniciar_vendedores,
            5: self.iniciar_notas_fiscais,
            0: self.finalizar
        }

        while True:
            try:
                opcao_escolhida = self.__tela_principal.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                
            except KeyError:
                self.__tela_principal.mostrar_mensagem(
                    "Voce digitou um numero invalido.")
            except ValueError:
                self.__tela_principal.mostrar_mensagem(
                    "Voce digitou um tipo invalido.")
            except TypeError:
                pass
