from excecoes.codigoVendedorInvalidoException import CodigoVendedorInvalidoException
from excecoes.cpfInvalidoException import CpfInvalidoException
from excecoes.nomeInvalidoException import NomeInvalidoException
from excecoes.vendedorJahExisteException import VendedorJahExisteException
from excecoes.vendedorNaoExisteException import VendedorNaoExisteException
from limite.telaVendedor import TelaVendedor
from entidade.vendedor import Vendedor


class ControladorVendedor:
  def __init__(self):
    self.__tela_vendedor = TelaVendedor([])
    self.__vendedores = []
    self.__codigo = 1

  def adicionar_vendedor(self):
    dados_vendedor = self.__tela_vendedor.pegar_dados_vendedor()

    cpf_vendedor = dados_vendedor["cpf_vendedor"]
    if not self.eh_cpf_valido(cpf_vendedor):
      raise CpfInvalidoException

    vendedor_encontrado = self.encontrar_vendedor_by_cpf(cpf_vendedor)
    if vendedor_encontrado:
      raise VendedorJahExisteException

    nome_vendedor = dados_vendedor["nome_vendedor"]
    if not self.eh_nome_valido(nome_vendedor):
      raise NomeInvalidoException

    codigo_vendedor = self.__codigo

    self.__codigo += 1

    vendedor = Vendedor(nome_vendedor, cpf_vendedor, codigo_vendedor)

    self.__vendedores.append(vendedor)
    self.__tela_vendedor.mostrar_mensagem(
        "O Vendedor foi cadastrado com sucesso!")

  def excluir_vendedor(self):
    codigo_vendedor = self.__tela_vendedor.selecionar_vendedor()
    if not self.eh_codigo_valido(codigo_vendedor):
      raise CodigoVendedorInvalidoException

    vendedor_encontrado = self.encontrar_vendedor(codigo_vendedor)
    if not vendedor_encontrado:
      raise VendedorNaoExisteException

    self.__vendedores.remove(vendedor_encontrado)
    self.__tela_vendedor.mostrar_mensagem(
        "O vendedor foi removido com sucesso!")

  def encontrar_vendedor(self, codigo_vendedor: int):
    for vendedor in self.__vendedores:
      if vendedor.codigo == codigo_vendedor:
        return vendedor

  def encontrar_vendedor_by_cpf(self, cpf_vendedor: int):
    for vendedor in self.__vendedores:
      if vendedor.cpf == cpf_vendedor:
        return vendedor

  def alterar_vendedor(self):
    codigo_vendedor = self.__tela_vendedor.selecionar_vendedor()
    if not self.eh_codigo_valido(codigo_vendedor):
      raise CodigoVendedorInvalidoException

    vendedor_encontrado = self.encontrar_vendedor(codigo_vendedor)
    if not vendedor_encontrado:
      raise VendedorNaoExisteException

    dados_vendedor = self.__tela_vendedor.pegar_dados_vendedor()

    nome_vendedor = dados_vendedor["nome_vendedor"]
    if not self.eh_nome_valido(nome_vendedor):
      raise NomeInvalidoException

    cpf_vendedor = dados_vendedor["cpf_vendedor"]
    if not self.eh_cpf_valido(cpf_vendedor):
      raise CpfInvalidoException

    vendedor_encontrado.nome = nome_vendedor
    vendedor_encontrado.cpf = cpf_vendedor

    self.__tela_vendedor.mostrar_mensagem(
        "O vendedor foi alterado com sucesso!")

  def listar_vendedores(self):
    dados_vendedores = []
    for vendedor in self.__vendedores:
      dados_vendedor = {
          "codigo_vendedor": vendedor.codigo,
          "nome_vendedor": vendedor.nome,
          "cpf_vendedor": vendedor.cpf
      }
      dados_vendedores.append(dados_vendedor)

    return dados_vendedores
    self.__tela_vendedor.mostrar_vendedores(dados_vendedores)

  def mostrar_tela_opcoes(self):
    opcoes = {
      1: self.adicionar_vendedor,
      2: self.listar_vendedores,
      3: self.alterar_vendedor,
      4: self.excluir_vendedor
    }

    while True:
      dados_vendedores = self.listar_vendedores()
      opcao = self.__tela_vendedor.mostrar_tela_opcoes(dados_vendedores)

      if opcao == 0:
        break

      try:
        opcoes[opcao]()
      except (VendedorJahExisteException, VendedorNaoExisteException, NomeInvalidoException, CpfInvalidoException) as err:
        self.__tela_vendedor.mostrar_mensagem(f"Erro: {err.args[0]}")

  def eh_nome_valido(self, nome_vendedor):
    return nome_vendedor.isalpha()

  def eh_cpf_valido(self, cpf_vendedor):
    return cpf_vendedor.isdigit() and isinstance(cpf_vendedor, int)
