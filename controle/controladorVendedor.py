from dtos.vendedor_dto import VendedorDto
from excecoes.codigoVendedorInvalidoException import CodigoVendedorInvalidoException
from excecoes.cpfInvalidoException import CpfInvalidoException
from excecoes.nomeInvalidoException import NomeInvalidoException
from excecoes.vendedorJahExisteException import VendedorJahExisteException
from excecoes.vendedorNaoExisteException import VendedorNaoExisteException
from limite.telaVendedor import TelaVendedor
from entidade.vendedor import Vendedor
from persistencia.vendedor_dao import VendedorDAO


class ControladorVendedor:
  def __init__(self):
    self.__tela_vendedor = TelaVendedor()
    self.__vendedor_dao = VendedorDAO()

  def adicionar_vendedor(self):
    vendedor_dto = self.__tela_vendedor.pegar_dados_vendedor()

    cpf = vendedor_dto.cpf
    if not self.eh_cpf_valido(cpf):
      raise CpfInvalidoException

    nome = vendedor_dto.nome
    if not self.eh_nome_valido(nome):
      raise NomeInvalidoException

    vendedor = Vendedor(nome, cpf)

    self.__vendedor_dao.adicionar(vendedor)
    self.__tela_vendedor.mostrar_mensagem(
        "O Vendedor foi cadastrado com sucesso!")

  def excluir_vendedor(self):
    codigo = self.__tela_vendedor.selecionar_vendedor()
    if not self.eh_codigo_valido(codigo):
      raise CodigoVendedorInvalidoException

    self.__vendedor_dao.remover(codigo)
    self.__tela_vendedor.mostrar_mensagem(
        "O vendedor foi removido com sucesso!")

  def encontrar_vendedor(self, codigo: int):
    return self.__vendedor_dao.encontrar(codigo)

  def alterar_vendedor(self):
    codigo = self.__tela_vendedor.selecionar_vendedor()

    print('erro aqui', codigo, type(codigo))
    vendedor_encontrado = self.encontrar_vendedor(codigo)
    print('2', vendedor_encontrado)
    if not vendedor_encontrado:
      raise VendedorNaoExisteException

    vendedor_dto = VendedorDto(vendedor_encontrado.nome, vendedor_encontrado.cpf, vendedor_encontrado.codigo)

    vendedor_dto = self.__tela_vendedor.alterar_dados_vendedor(vendedor_dto)

    nome = vendedor_dto.nome
    if not self.eh_nome_valido(nome):
      raise NomeInvalidoException

    vendedor_encontrado.nome = nome

    self.__vendedor_dao.atualizar(vendedor_encontrado)
    self.__tela_vendedor.mostrar_mensagem(
        "O vendedor foi alterado com sucesso!")

  def listar_vendedores(self):
    vendedores_dtos = []
    vendedores = self.__vendedor_dao.listar()
    for vendedor in vendedores:
      vendedor_dto = VendedorDto(vendedor.nome, vendedor.cpf, vendedor.codigo)
           
      vendedores_dtos.append(vendedor_dto)

    self.__tela_vendedor.mostrar_vendedores(vendedores_dtos)

  def mostrar_tela_opcoes(self):
    opcoes = {
      1: self.adicionar_vendedor,
      2: self.listar_vendedores,
      3: self.alterar_vendedor,
      4: self.excluir_vendedor
    }

    while True:
      opcao = self.__tela_vendedor.mostrar_tela_opcoes()

      if opcao == 0:
        break

      try:
        opcoes[opcao]()
      except (VendedorJahExisteException, VendedorNaoExisteException, NomeInvalidoException, CpfInvalidoException) as err:
        self.__tela_vendedor.mostrar_mensagem(f"Erro: {err.args[0]}")

  def eh_nome_valido(self, nome):
    return nome.isalpha()

  def eh_cpf_valido(self, cpf):
    return isinstance(cpf, int)

  def eh_codigo_valido(self, codigo):
    return isinstance(codigo, int)
