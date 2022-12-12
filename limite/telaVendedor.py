import PySimpleGUI as sg
from dtos.vendedor_dto import VendedorDto
from limite.componentes.componente_listagem import ComponenteListagem
from limite.componentes.componente_opcoes import ComponenteOpcoes
from limite.componentes.componente_vendedor_cadastro import ComponenteVendedorCadastro
from limite.componentes.componente_vendedor_edicao import ComponenteVendedorEdicao
from limite.componentes.componente_vendedor_selecao import ComponenteVendedorSelecao

class TelaVendedor:
  def __init__(self):
    self.__window = self.criar_tela_opcoes()

  def mostrar_tela_opcoes(self):
    self.__window = self.criar_tela_opcoes()
    opcao = None
    button, values = self.open()
    if values['1']:
      opcao = 1
    elif values['2']:
      opcao = 2
    elif values['3']:
      opcao = 3
    elif values['4']:
      opcao = 4
    if values['0'] or button in (None, 'Voltar'):
      opcao = 0
    self.close()
    return opcao
    
  def criar_tela_opcoes(self):
    return ComponenteOpcoes('vendedores').container

  def criar_tela_dados(self):
    return ComponenteVendedorCadastro().container

  def criar_tela_listagem(self, dados_vendedores):
    return ComponenteListagem('vendedores', dados_vendedores).container

  def criar_tela_selecao(self):
    return ComponenteVendedorSelecao().container

  def criar_tela_edicao(self, vendedor_dto):
    return ComponenteVendedorEdicao(vendedor_dto).container

  def mostrar_vendedores(self, vendedores_dtos):
    self.__window = self.criar_tela_listagem(vendedores_dtos)

    button, _ = self.open()
    while True:
      if button in (sg.WIN_CLOSED, 'Voltar'):
        break

    self.close()

  def mostrar_mensagem(self, mensagem):
    sg.popup("", mensagem)

  def pegar_dados_vendedor(self):
    self.__window = self.criar_tela_dados()
    button, _ = self.open()
    while True:
      if button in (sg.WIN_CLOSED, 'Cancelar'):
        self.close()
        break
      try:
        vendedor = self.pegar_vendedor()
        self.close()

        return vendedor
      except ValueError:
        self.mostrar_mensagem('Dado invalido!')

  def pegar_vendedor(self):
    _, values = self.open()

    nome = values['it_cadasto_vendedor_nome']
    cpf = int(values['it_cadasto_vendedor_cpf'])

    vendedor_dto = VendedorDto(nome, cpf)

    return vendedor_dto

  def selecionar_vendedor(self):
    self.__window = self.criar_tela_selecao()

    while True:
      try:
        _, values = self.open()
        cpf_vendedor = int(values['it_selecao_vendedor_codigo'])
        self.close()

        return cpf_vendedor
      except ValueError:
        self.mostrar_mensagem('Dado invalido!')

  def alterar_dados_vendedor(self, vendedor_dto):
      self.__window = self.criar_tela_edicao(vendedor_dto)
      while True:
        try:
          vendedor = self.alterar_vendedor()
          self.close()

          return vendedor
        except ValueError:
          self.mostrar_mensagem('Dado invalido!')

  def alterar_vendedor(self):
    _, values = self.open()

    nome = values['it_edicao_vendedor_nome']

    vendedor_dto = VendedorDto(nome)

    return vendedor_dto

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
