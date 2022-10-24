from limite.telaVendedor import TelaVendedor
from entidade.vendedor import Vendedor


class ControladorVendedor:
  def __init__(self, controlador_principal):
    #self.__controlador_principal = controlador_principal
    self.__tela_vendedor = TelaVendedor()
    self.__vendedores = []

  def adicionar_vendedor(self, vendedor: Vendedor):
    dados_vendedor = self.__tela_vendedor.pega_dados_vendedor()
    if not dados_vendedor and isinstance(vendedor, Vendedor):
      self.__vendedores.append(vendedor)

  def excluir_vendedor(self, codigo_vendedor: int):
    vendedor_encontrado = self.codigo_vendedor(codigo_vendedor)
    if vendedor_encontrado:
      self.__vendedores.remove(vendedor_encontrado)

  def encontrar_codigo_vendedor(self, codigo_vendedor: int):
    for vendedor in self.__vendedores:
      if vendedor.codigo_vendedor == codigo_vendedor:
        return vendedor